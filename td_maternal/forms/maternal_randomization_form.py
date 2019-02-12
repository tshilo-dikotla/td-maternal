from django import forms
from td_maternal_validators.form_validators import MaternalRandoFormValidator

from ..models import MaternalRando
from .form_mixins import SubjectModelFormMixin


class MaternalRandomizationForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalRandoFormValidator

    class Meta:
        model = MaternalRando
        fields = '__all__'
