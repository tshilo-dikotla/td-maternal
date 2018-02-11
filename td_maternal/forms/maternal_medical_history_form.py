from django import forms
from ..models import MaternalMedicalHistory
from .form_mixins import SubjectModelFormMixin


class MaternalMedicalHistoryForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalMedicalHistory
        fields = '__all__'
