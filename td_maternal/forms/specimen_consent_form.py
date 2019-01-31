from django import forms

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import SpecimenConsent


class SpecimenConsentForm(SiteModelFormMixin, FormValidatorMixin,
                          forms.ModelForm):

    class Meta:
        model = SpecimenConsent
        fields = '__all__'
