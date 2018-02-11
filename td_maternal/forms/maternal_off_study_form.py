from django import forms
from ..models import MaternalOffStudy


class MaternalOffStudyForm(forms.ModelForm):

    class Meta:
        model = MaternalOffStudy
        fields = '__all__'
