from django import forms
from td_maternal_validators.form_validators import MaternalSubstanceUseDuringPregFormValidator
from ..models import MaternalSubstanceUseDuringPreg
from .form_mixins import SubjectModelFormMixin


class MaternalSubstanceUseDuringPregForm(
        SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalSubstanceUseDuringPregFormValidator

    class Meta:
        model = MaternalSubstanceUseDuringPreg
        fields = '__all__'
