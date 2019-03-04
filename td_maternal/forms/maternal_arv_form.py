from django import forms
from django.core.exceptions import ValidationError

from td_maternal_validators.form_validators import MaternalArvFormValidator

from ..models import MaternalArv
from .form_mixins import SubjectModelFormMixin


class MaternalArvForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalArvFormValidator

    class Meta:
        model = MaternalArv
        fields = '__all__'
