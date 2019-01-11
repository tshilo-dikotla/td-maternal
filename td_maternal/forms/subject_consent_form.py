from django import forms
from django.conf import settings
from edc_base.sites import SiteModelFormMixin
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_constants.constants import FEMALE
from edc_form_validators import FormValidatorMixin
from td_maternal_validators.form_validators import MaternalConsentFormValidator

from ..choices import STUDY_SITES
from ..models import SubjectConsent


class SubjectConsentForm(
        SiteModelFormMixin, FormValidatorMixin, ConsentModelFormMixin,
        forms.ModelForm):

    form_validator_cls = MaternalConsentFormValidator

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    study_site = forms.ChoiceField(
        label='Study site',
        choices=STUDY_SITES,
        initial=settings.DEFAULT_STUDY_SITE,
        widget=forms.RadioSelect)

    def clean(self):
        self.cleaned_data['gender'] = FEMALE

    class Meta:
        model = SubjectConsent
        fields = '__all__'
