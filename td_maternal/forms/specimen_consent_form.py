from django import forms
from ..models import SpecimenConsent


class SpecimenConsentForm(forms.ModelForm):

    class Meta:
        model = SpecimenConsent
        fields = '__all__'
