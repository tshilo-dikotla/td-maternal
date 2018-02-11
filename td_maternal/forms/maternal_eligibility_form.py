from django import forms
from ..models import MaternalEligibility


class MaternalEligibilityForm(forms.ModelForm):

    class Meta:
        model = MaternalEligibility
        fields = '__all__'
