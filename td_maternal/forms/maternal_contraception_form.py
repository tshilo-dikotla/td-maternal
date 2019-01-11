from django import forms
from td_maternal_validators.form_validators import MaternalContraceptionFormValidator

from ..models import MaternalContraception
from .form_mixins import SubjectModelFormMixin


class MaternalContraceptionForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalContraceptionFormValidator

    class Meta:
        model = MaternalContraception
        fields = '__all__'
