from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import SubjectConsent


class SubjectConsentForm(
        SiteModelFormMixin, FormValidatorMixin, ConsentModelFormMixin,
        forms.ModelForm):

    #     study_site = forms.ChoiceField(
    #         label='Study site',
    #         choices=STUDY_SITES,
    #         initial=settings.DEFAULT_STUDY_SITE,
    #         help_text="",
    #         widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    class Meta:
        model = SubjectConsent
        fields = '__all__'
