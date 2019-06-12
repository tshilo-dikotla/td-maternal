from django import forms
from edc_form_validators import FormValidatorMixin
from td_maternal_validators.form_validators import (
    KaraboSubjectScreeningFormValidator)

from ..models import KaraboSubjectScreening


class KaraboSubjectScreeningForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = KaraboSubjectScreeningFormValidator

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = KaraboSubjectScreening
        fields = '__all__'
