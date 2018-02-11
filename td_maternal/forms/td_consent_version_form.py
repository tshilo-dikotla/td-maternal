from django import forms
from ..models import TdConsentVersion


class TdConsentVersionForm(forms.ModelForm):

    class Meta:
        model = TdConsentVersion
        fields = '__all__'
