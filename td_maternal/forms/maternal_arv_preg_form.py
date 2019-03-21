from django import forms
from django.apps import apps as django_apps
from edc_constants.constants import YES
from td_maternal_validators.form_validators import MaternalArvPregFormValidator

from ..models import MaternalArvPreg
from .form_mixins import SubjectModelFormMixin

import datetime


class MaternalArvPregForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalArvPregFormValidator

    antenatal_enrollment_model = 'td_maternal.antenatalenrollment'
    appointment = 'edc_appointment.appointment'
    maternal_arv = 'td_maternal.maternalarv'
    maternal_preg = 'td_maternal.maternalarvpreg'

    @property
    def appointment_cls(self):
        return django_apps.get_model(self.appointment)

    @property
    def maternal_arv_cls(self):
        return django_apps.get_model(self.maternal_arv)

    @property
    def maternal_preg_cls(self):
        return django_apps.get_model(self.maternal_preg)

    @property
    def antenatal_enrollment_cls(self):
        return django_apps.get_model(self.antenatal_enrollment_model)

    def clean(self):
        cleaned_data = super().clean()
        maternal_arv = self.data.get(
            'maternalarv_set-0-arv_code')
        if cleaned_data.get('took_arv') and\
                cleaned_data.get('took_arv') == YES:
            if not maternal_arv:
                raise forms.ValidationError(
                    {'took_arv': 'Please complete the maternal arv table.'})

        self.validate_num_arvs_taken()
        self.validate_date_arv_stopped()
        self.validate_arv_date_start_after_enrollment()
        self.validate_previous_maternal_arv_preg_arv_start_dates()
        self.validate_repeating_arvs()
        return cleaned_data

    def validate_num_arvs_taken(self):
        maternal_arv_count = self.data.get(
            'maternalarv_set-TOTAL_FORMS')
        if int(maternal_arv_count) < 3:
            raise forms.ValidationError(
                'Patient should have more than 3 arv\'s')

    def validate_date_arv_stopped(self):
        maternal_arv_count = self.data.get(
            'maternalarv_set-TOTAL_FORMS')
        arvs_with_stop_date = 0
        for i in range(int(maternal_arv_count)):
            maternal_arv = self.data.get(
                'maternalarv_set-' + str(i) + '-stop_date')
            if maternal_arv:
                arvs_with_stop_date = \
                    arvs_with_stop_date + 1
        if (int(maternal_arv_count) - arvs_with_stop_date) < 3:
                raise forms.ValidationError(
                    'Patient should have more than 3 arv\'s in progress')

    def validate_arv_date_start_after_enrollment(self):
        try:
            antenatal_enrollment = self.antenatal_enrollment_cls.objects.get(
                subject_identifier=self.cleaned_data.get(
                    'maternal_visit').subject_identifier)
        except self.antenatal_enrollment_cls.DoesNotExist:
            raise forms.ValidationError(
                'Date of HIV test required, complete Antenatal Enrollment'
                ' form before proceeding.')
        else:
            maternal_arv_count = self.data.get(
                'maternalarv_set-TOTAL_FORMS')
            for i in range(int(maternal_arv_count)):
                if self.data.get('maternalarv_set-' + str(i) + '-start_date'):
                    set_start_date = self.data.get(
                        'maternalarv_set-' + str(i) + '-start_date')
                    date_time_obj = datetime.datetime.strptime(set_start_date,
                                                               '%Y-%m-%d')
                    if date_time_obj.date() < \
                            antenatal_enrollment.week32_test_date:
                        raise forms.ValidationError(
                            'start date of arv\'s '
                            'cannot be before date of HIV test.')

    def get_previous_visit(self, visit_obj, timepoints, subject_identifier):
        position = timepoints.index(
            visit_obj.appointment.visit_code)
        timepoints_slice = timepoints[:position]
        visit_model = django_apps.get_model(visit_obj._meta.label_lower)

        if len(timepoints_slice) > 1:
            timepoints_slice.reverse()

        for point in timepoints_slice:
            try:
                previous_appointment = self.appointment_cls.objects.filter(
                    subject_identifier=subject_identifier,
                    visit_code=point).order_by('-created').first()
                return visit_model.objects.filter(
                    appointment=previous_appointment
                ).order_by('-created').first()
            except self.appointment_cls.DoesNotExist:
                pass
            except visit_model.DoesNotExist:
                pass
            except AttributeError:
                pass
        return None

    def validate_previous_maternal_arv_preg_arv_start_dates(self):
        """Confirms that the ARV start date is equal to Maternal ARV
        start date unless stopped.
        """
        cleaned_data = self.cleaned_data
        subject_identifier = cleaned_data.get(
            'maternal_visit').appointment.subject_identifier
        previous_visit = self.get_previous_visit(
            visit_obj=cleaned_data.get('maternal_visit'),
            timepoints=['1000M', '1020M', '2000M'],
            subject_identifier=subject_identifier)

        if previous_visit:
            previous_arv_preg = self.maternal_arv_cls.objects.filter(
                maternal_arv_preg__maternal_visit__appointment__subject_identifier=\
                subject_identifier,
                stop_date__isnull=True).order_by('-start_date').first()

            if previous_arv_preg:
                if previous_arv_preg.start_date:
                    arv_count = self.data.get('maternalarv_set-TOTAL_FORMS')

                    for index in range(int(arv_count)):
                        start_date = self.data.get(
                            'maternalarv_set-' + str(index) + '-start_date')
                        if start_date:
                            start_date = datetime.datetime.strptime(
                                start_date, '%Y-%m-%d')
                            if start_date.date() != previous_arv_preg.start_date:
                                raise forms.ValidationError(
                                    "ARV's were not stopped in this pregnancy,"
                                    " most recent ARV date was "
                                    "{}, dates must match, got {}.".format(
                                        previous_arv_preg.start_date,
                                        start_date.date()))

    def validate_repeating_arvs(self):
        arv_count = int(self.data.get('maternalarv_set-TOTAL_FORMS'))
        unique_arvs = []
        for index in range(arv_count):
            arv_code = self.data.get(
                'maternalarv_set-' + str(index) + '-arv_code')
            if arv_code and arv_code in unique_arvs:
                raise forms.ValidationError(
                    "ARV's cannot be duplicated,"
                    " Please correct arv's in the table below "
                )
            else:
                unique_arvs.append(arv_code)

    class Meta:
        model = MaternalArvPreg
        fields = '__all__'
