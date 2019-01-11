from django import forms
from td_maternal_validators.form_validators import RapidTestResultFormValidator
from ..models import RapidTestResult
from .form_mixins import SubjectModelFormMixin


class RapidTestResultForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = RapidTestResultFormValidator

    class Meta:
        model = RapidTestResult
        fields = '__all__'
