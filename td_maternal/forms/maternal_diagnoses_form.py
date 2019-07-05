from django import forms
from td_maternal_validators.form_validators import MaternalDiagnosesFormValidator

from ..models import MaternalDiagnoses
from .form_mixins import SubjectModelFormMixin


class MaternalDiagnosesForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalDiagnosesFormValidator

    class Meta:
        model = MaternalDiagnoses
        fields = '__all__'
