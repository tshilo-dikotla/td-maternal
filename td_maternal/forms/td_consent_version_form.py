from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from td_maternal_validators.form_validators import TDConsentVersionFormValidator

from ..models import TdConsentVersion


class TdConsentVersionForm(SiteModelFormMixin, FormValidatorMixin,
                           forms.ModelForm):

    form_validator_cls = TDConsentVersionFormValidator

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = TdConsentVersion
        fields = '__all__'
