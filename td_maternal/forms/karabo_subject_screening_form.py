from django import forms
from ..models import KaraboSubjectScreening


class KaraboSubjectScreeningForm(forms.ModelForm):

    # form_validator_cls = 

    class Meta:
        model = KaraboSubjectScreening
        fields = '__all__'
