from django import forms
from td_maternal_validators.form_validators import MaternalUltrasoundInitialFormValidator
from ..models import MaternalUltraSoundInitial
from .form_mixins import SubjectModelFormMixin


class MaternalUltraSoundInitialForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalUltrasoundInitialFormValidator

    class Meta:
        model = MaternalUltraSoundInitial
        fields = '__all__'
