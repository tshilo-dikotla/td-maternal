from django import forms
from td_maternal_validators.form_validators import MaternalHivInterimHxFormValidator
from .form_mixins import SubjectModelFormMixin
from ..models import MaternalHivInterimHx


class MaternalHivInterimHxForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalHivInterimHxFormValidator

    class Meta:
        model = MaternalHivInterimHx
        fields = '__all__'
