from django import forms
from ..models import MaternalLocator


class MaternalLocatorForm(forms.ModelForm):

    class Meta:
        model = MaternalLocator
        fields = '__all__'
