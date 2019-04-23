from django import forms
from td_maternal_validators.form_validators import MaternalSrhFormValidator
from ..models import MaternalSrh
from .form_mixins import SubjectModelFormMixin


class MaternalSrhForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalSrhFormValidator

    class Meta:
        model = MaternalSrh
        fields = '__all__'
