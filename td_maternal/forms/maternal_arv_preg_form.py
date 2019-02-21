from django import forms
from edc_constants.constants import YES
from td_maternal_validators.form_validators import MaternalArvPregFormValidator

from ..models import MaternalArvPreg
from .form_mixins import SubjectModelFormMixin


class MaternalArvPregForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalArvPregFormValidator

    def clean(self):
        cleaned_data = super().clean()
        maternal_arv = self.data.get(
            'maternalarv_set-0-arv_code')
        if cleaned_data.get('took_arv') and cleaned_data.get('took_arv') == YES:
            if not maternal_arv:
                raise forms.ValidationError(
                    {'took_arv': 'Please complete the maternal arv table.'})
        return cleaned_data

    class Meta:
        model = MaternalArvPreg
        fields = '__all__'
