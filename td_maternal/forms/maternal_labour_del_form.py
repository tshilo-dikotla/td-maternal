from django import forms
from ..models import MaternalLabourDel


class MaternalLabourDelForm(forms.ModelForm):

    class Meta:
        model = MaternalLabourDel
        fields = '__all__'
