from django import forms
from edc_constants.constants import NEW
from td_maternal_validators.form_validators import MarternalArvPostFormValidator

from ..models import MaternalArvPost, MaternalArvPostMed, MaternalArvPostAdh

from .form_mixins import SubjectModelFormMixin


class MaternalArvPostForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MarternalArvPostFormValidator

    def clean(self):
        cleaned_data = super().clean()
        arv_code = self.data.get('maternalarvpostmed_set-0-arv_code')

        if cleaned_data.get('arv_status') == 'modified' and not arv_code:
                    raise forms.ValidationError(
                        {'arv_status':
                         'Please complete the maternal arv table.'})
        self.validate_arv_modified()

    def validate_arv_modified(self):
        total_arvs = int(self.data.get('maternalarvpostmed_set-TOTAL_FORMS'))

        for i in range(total_arvs):
            modification_date = self.data.get(
                'maternalarvpostmed_set-' + str(i) + '-modification_date')
            arv_status = self.data.get(
                'maternalarvpostmed_set-' + str(i) + '-dose_status')

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

    class Meta:
        model = MaternalArvPost
        fields = '__all__'


class MaternalArvPostMedForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalArvPostMed
        fields = '__all__'


class MaternalArvPostAdhForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalArvPostAdh
        fields = '__all__'
