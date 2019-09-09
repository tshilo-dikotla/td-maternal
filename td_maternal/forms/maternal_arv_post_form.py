from django import forms
from django.apps import apps as django_apps
from edc_constants.constants import NEW

from td_maternal_validators.form_validators import MarternalArvPostFormValidator
from td_maternal_validators.form_validators import TDCRFFormValidator

from ..models import MaternalArvPost, MaternalArvPostMed, MaternalArvPostAdh
from .form_mixins import SubjectModelFormMixin


class MaternalArvPostForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MarternalArvPostFormValidator

    maternal_arv = 'td_maternal.maternalarv'

    def clean(self):
        cleaned_data = super().clean()
        arv_code = self.data.get('maternalarvpostmed_set-0-arv_code')

        if cleaned_data.get('arv_status') == 'modified' and not arv_code:
            raise forms.ValidationError(
                {'arv_status':
                 'Please complete the maternal arv table.'})

        self.validate_arv_modified()
        self.validate_arv_history()

    def validate_arv_modified(self):
        total_arvs = int(self.data.get('maternalarvpostmed_set-TOTAL_FORMS'))

        for i in range(total_arvs):
            modification_date = self.data.get(
                'maternalarvpostmed_set-' + str(i) + '-modification_date')
            arv_status = self.data.get(
                'maternalarvpostmed_set-' + str(i) + '-dose_status')

            mod_code = self.data.get(
                'maternalarvpostmed_set-' + str(i) + '-modification_code')

            if mod_code not in ['Non-adherence with ARVs']:
                if (arv_status == NEW and
                        modification_date != self.get_arv_modification_date()):
                    raise forms.ValidationError(
                        {'arv_status': 'Modification date of new ARV should be'
                         ' same as ARV permanently discountinued date'})

    def get_arv_modification_date(self):
        total_arvs = int(self.data.get('maternalarvpostmed_set-TOTAL_FORMS'))

        for i in range(total_arvs):
            arv_status = self.data.get(
                'maternalarvpostmed_set-' + str(i) + '-dose_status')
            modification_date = self.data.get(
                'maternalarvpostmed_set-' + str(i) + '-modification_date')

            if arv_status == 'Permanently discontinued' and modification_date:
                return modification_date

    def validate_arv_history(self):
        arvs = self.get_all_arvs()
        arv_codes = []
        total_arvs = int(self.data.get('maternalarvpostmed_set-TOTAL_FORMS'))

        if arvs:
            for arv in arvs:
                arv_codes.append(arv.arv_code)

        for i in range(total_arvs):
            arv_code = self.data.get(
                'maternalarvpostmed_set-' + str(i) + '-arv_code')
            arv_status = self.data.get(
                'maternalarvpostmed_set-' + str(i) + '-dose_status')
            if arv_code and not (arv_code in arv_codes):
                if not (arv_status == NEW):
                    raise forms.ValidationError(
                        {'arv_status':
                         'Patient have not taking ARV ' + arv_code})

    def get_all_arvs(self):
        subject_identifier = self.cleaned_data.get(
            'maternal_visit').appointment.subject_identifier
        try:
            maternal_arvs = self.maternal_arv_cls.objects.filter(
                maternal_arv_preg__maternal_visit__appointment__subject_identifier=subject_identifier, stop_date__isnull=True)
        except self.maternal_arv_cls.DoesNotExist:
            raise forms.ValidationError(
                'Participant have not started arv\'s yet')
        else:
            return maternal_arvs

    @property
    def maternal_arv_cls(self):
        return django_apps.get_model(self.maternal_arv)

    class Meta:
        model = MaternalArvPost
        fields = '__all__'


class MaternalArvPostMedForm(SubjectModelFormMixin, forms.ModelForm):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'maternal_arv_post').maternal_visit.appointment.subject_identifier

    class Meta:
        model = MaternalArvPostMed
        fields = '__all__'


class MaternalArvPostAdhForm(SubjectModelFormMixin, TDCRFFormValidator,
                             forms.ModelForm):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'maternal_visit').subject_identifier
        if self.instance and not self.instance.id:
            self.validate_offstudy_model()

    class Meta:
        model = MaternalArvPostAdh
        fields = '__all__'
