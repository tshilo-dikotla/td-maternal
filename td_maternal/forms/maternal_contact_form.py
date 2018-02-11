from django import forms
from ..models import MaternalContact


class MaternalContactForm(forms.ModelForm):

    class Meta:
        model = MaternalContact
        fields = '__all__'
