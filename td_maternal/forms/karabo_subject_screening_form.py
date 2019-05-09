from django import forms
from ..models import KaraboSubjectScreening


class KaraboSubjectScreeningForm(forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = KaraboSubjectScreening
        fields = '__all__'
