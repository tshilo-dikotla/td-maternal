from django import forms
from ..models import AntenatalEnrollment


class AntenatalEnrollmentForm(forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = AntenatalEnrollment
        fields = '__all__'
