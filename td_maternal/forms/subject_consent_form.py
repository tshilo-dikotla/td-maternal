from django import forms
from django.conf import settings
from edc_base.sites import SiteModelFormMixin
from edc_consent.exceptions import ConsentObjectDoesNotExist
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_consent.site_consents import site_consents, SiteConsentError
from edc_constants.constants import FEMALE
from edc_form_validators import FormValidatorMixin

from td_maternal_validators.form_validators import SubjectConsentFormValidator

from ..models import SubjectConsent


class SubjectConsentForm(
        SiteModelFormMixin, FormValidatorMixin, ConsentModelFormMixin,
        forms.ModelForm):

    form_validator_cls = SubjectConsentFormValidator

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    @property
    def consent_config(self):
        cleaned_data = self.cleaned_data
        try:
            consent_config = site_consents.get_consent(
                report_datetime=cleaned_data.get(
                    'consent_datetime') or self.instance.consent_datetime,
                consent_model=self._meta.model._meta.label_lower,
                model=self._meta.model._meta.label_lower,
                consent_group=self._meta.model._meta.consent_group
            )
        except (ConsentObjectDoesNotExist, SiteConsentError) as e:
            raise forms.ValidationError(e)
        return consent_config

    def clean(self):
        self.cleaned_data['gender'] = FEMALE
        self.cleaned_data['study_site'] = settings.DEFAULT_STUDY_SITE
        super().clean()

    class Meta:
        model = SubjectConsent
        fields = '__all__'
