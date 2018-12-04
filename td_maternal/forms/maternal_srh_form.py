from django import forms
from ..models import MaternalSrh


class MaternalSrhForm(forms.ModelForm):

    class Meta:
        model = MaternalSrh
        fields = '__all__'
