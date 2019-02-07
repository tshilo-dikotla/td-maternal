from td_maternal.forms.form_mixins import SubjectModelFormMixin
from django import forms
from td_maternal_validators.form_validators import TDConsentVersionFormValidator

from ..models import TdConsentVersion


class TdConsentVersionForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = TDConsentVersionFormValidator

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = TdConsentVersion
        fields = '__all__'
