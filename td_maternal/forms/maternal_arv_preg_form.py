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

    class Meta:
        model = MaternalArvPreg
        fields = '__all__'
