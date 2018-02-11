from django import forms
from ..models import MaternalDiagnoses
from .form_mixins import SubjectModelFormMixin


class MaternalDiagnosesForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalDiagnoses
        fields = '__all__'
