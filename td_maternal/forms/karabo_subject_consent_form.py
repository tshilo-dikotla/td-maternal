from django import forms
from ..models import KaraboSubjectConsent


class KaraboSubjectConsentForm(forms.ModelForm):

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = KaraboSubjectConsent
        fields = '__all__'
