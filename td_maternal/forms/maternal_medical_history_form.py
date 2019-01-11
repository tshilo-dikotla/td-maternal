from django import forms
from td_maternal_validators.form_validators import MaternalMedicalHistoryFormValidator
from ..models import MaternalMedicalHistory
from .form_mixins import SubjectModelFormMixin


class MaternalMedicalHistoryForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalMedicalHistoryFormValidator

    class Meta:
        model = MaternalMedicalHistory
        fields = '__all__'
