from django import forms
from edc_form_validators import FormValidatorMixin
from ..models import KaraboSubjectConsent
from td_maternal_validators.form_validators import (
    KaraboSubjectConsentFormValidator)


class KaraboSubjectConsentForm(FormValidatorMixin):

    form_validator_cls = KaraboSubjectConsentFormValidator

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = KaraboSubjectConsent
        fields = '__all__'
