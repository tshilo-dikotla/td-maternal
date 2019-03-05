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
        self.validate_start_date_in_visit_1020()
        return cleaned_data

    def validate_num_arvs_taken(self):
        maternal_arv = self.data.get(
            'maternalarv_set-0-arv_code')
        maternal_arv_1 = self.data.get(
            'maternalarv_set-1-arv_code')
        maternal_arv_2 = self.data.get(
            'maternalarv_set-2-arv_code')

        if not (maternal_arv and maternal_arv_1 and maternal_arv_2):
            raise forms.ValidationError(
                'Patient should have more than 3 arv\'s')

    def validate_date_arv_stopped(self):
        maternal_arv = self.data.get(
            'maternalarv_set-0-stop_date')
        maternal_arv_1 = self.data.get(
            'maternalarv_set-1-stop_date')
        maternal_arv_2 = self.data.get(
            'maternalarv_set-2-stop_date')
        maternal_arv_3 = self.data.get(
            'maternalarv_set-3-start_date')
        if maternal_arv or maternal_arv_1 or maternal_arv_2:
            if not maternal_arv_3:
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
            if self.data.get('maternalarv_set-0-start_date'):
                set_0_start_date = self.data.get(
                    'maternalarv_set-0-start_date')
                date_time_obj = datetime.datetime.strptime(set_0_start_date,
                                                           '%Y-%m-%d')
                if date_time_obj.date() < \
                        antenatal_enrollment.week32_test_date:
                    raise forms.ValidationError(
                        'start date of arv\'s '
                        'cannot be before date of HIV test.')

            if self.data.get('maternalarv_set-1-start_date'):
                set_1_start_date = self.data.get(
                    'maternalarv_set-1-start_date')
                date_time_obj = datetime.datetime.strptime(set_1_start_date,
                                                           '%Y-%m-%d')
                if date_time_obj.date() < \
                        antenatal_enrollment.week32_test_date:
                    raise forms.ValidationError(
                        'start date of arv\'s '
                        'cannot be before date of HIV test.')

            if self.data.get('maternalarv_set-2-start_date'):
                set_2_start_date = self.data.get(
                    'maternalarv_set-2-start_date')
                date_time_obj = datetime.datetime.strptime(set_2_start_date,
                                                           '%Y-%m-%d')
                if date_time_obj.date() < \
                        antenatal_enrollment.week32_test_date:
                    raise forms.ValidationError(
                        'start date of arv\'s '
                        'cannot be before date of HIV test.')

            if self.data.get('maternalarv_set-3-start_date'):
                set_3_start_date = self.data.get(
                    'maternalarv_set-3-start_date')
                date_time_obj = datetime.datetime.strptime(set_3_start_date,
                                                           '%Y-%m-%d')
                if date_time_obj.date() < \
                        antenatal_enrollment.week32_test_date:
                    raise forms.ValidationError(
                        'start date of arv\'s '
                        'cannot be before date of HIV test.')

    def validate_start_date_in_visit_1020(self):
        visit_code = self.cleaned_data.get('maternal_visit').appointment.visit_code
        if visit_code == '1020M':
            if self.data.get('maternalarv_set-0-start_date'):
                set_0_start_date = self.data.get(
                    'maternalarv_set-0-start_date')
                date_time_obj = datetime.datetime.strptime(set_0_start_date,
                                                           '%Y-%m-%d')
                if not (date_time_obj.date() == 
                        self.cleaned_data.get('report_datetime').date()):
                    raise forms.ValidationError(
                        'start date of arv\'s '
                        'cannot be before date of HIV test.')

            if self.data.get('maternalarv_set-1-start_date'):
                set_1_start_date = self.data.get(
                    'maternalarv_set-1-start_date')
                date_time_obj = datetime.datetime.strptime(set_1_start_date,
                                                           '%Y-%m-%d')
                if not (date_time_obj.date() == 
                        self.cleaned_data.get('report_datetime').date()):
                    raise forms.ValidationError(
                        'start date of arv\'s '
                        'cannot be before date of HIV test.')

            if self.data.get('maternalarv_set-2-start_date'):
                set_2_start_date = self.data.get(
                    'maternalarv_set-2-start_date')
                date_time_obj = datetime.datetime.strptime(set_2_start_date,
                                                           '%Y-%m-%d')
                if not (date_time_obj.date() == 
                        self.cleaned_data.get('report_datetime').date()):
                    raise forms.ValidationError(
                        'start date of arv\'s '
                        'cannot be before date of HIV test.')

            if self.data.get('maternalarv_set-3-start_date'):
                set_3_start_date = self.data.get(
                    'maternalarv_set-3-start_date')
                date_time_obj = datetime.datetime.strptime(set_3_start_date,
                                                           '%Y-%m-%d')
                if not (date_time_obj.date() == 
                        self.cleaned_data.get('report_datetime').date()):
                    raise forms.ValidationError(
                        'start date of arv\'s '
                        'cannot be before date of HIV test.')
        pass

    class Meta:
        model = MaternalArvPreg
        fields = '__all__'
