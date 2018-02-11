from django import forms
from ..models import AntenatalEnrollment


class AntenatalEnrollmentForm(forms.ModelForm):

    class Meta:
        model = AntenatalEnrollment
        fields = '__all__'
