from django import forms
from ..models import KaraboSubjectConsent


class KaraboSubjectConsentForm(forms.ModelForm):

    # form_validator_cls = 

    class Meta:
        model = KaraboSubjectConsent
        fields = '__all__'
