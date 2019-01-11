from django import forms
from td_maternal_validators.form_validators import MaternalSubstanceUsePriorPregFormValidator
from ..models import MaternalSubstanceUsePriorPreg
from .form_mixins import SubjectModelFormMixin


class MaternalSubstanceUsePriorPregForm(
        SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalSubstanceUsePriorPregFormValidator

    class Meta:
        model = MaternalSubstanceUsePriorPreg
        fields = '__all__'
