from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_consent.modelform_mixins import RequiresConsentModelFormMixin
from edc_form_validators import FormValidatorMixin

from td_maternal_validators.form_validators import SpecimenConsentFormValidator

from ..models import SpecimenConsent


class SpecimenConsentForm(SiteModelFormMixin, FormValidatorMixin,
                          forms.ModelForm):

    form_validator_cls = SpecimenConsentFormValidator

    class Meta:
        model = SpecimenConsent
        fields = '__all__'
