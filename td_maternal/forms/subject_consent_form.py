from django import forms
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ValidationError
from edc_base.sites import SiteModelFormMixin
from edc_constants.constants import FEMALE
from edc_form_validators import FormValidatorMixin
from edc_consent.modelform_mixins import ConsentModelFormMixin
from td_maternal_validators.form_validators import SubjectConsentFormValidator

from ..models import SubjectConsent


class SubjectConsentForm(
        SiteModelFormMixin, FormValidatorMixin, ConsentModelFormMixin,
        forms.ModelForm):

    form_validator_cls = SubjectConsentFormValidator

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        self.cleaned_data['gender'] = FEMALE
        self.cleaned_data['study_site'] = settings.DEFAULT_STUDY_SITE
        self.cleaned_data['version'] = self.consent_version
        super().clean()

    @property
    def consent_version(self):
        consent_version_cls = django_apps.get_model(
            'td_maternal.tdconsentversion')
        try:
            consent_version_obj = consent_version_cls.objects.get(
                screening_identifier=self.cleaned_data.get('screening_identifier'))
        except consent_version_cls.DoesNotExist:
            raise ValidationError(
                'Missing Consent Version form. Please complete '
                'it before proceeding.')
        return consent_version_obj.version

    class Meta:
        model = SubjectConsent
        fields = '__all__'
