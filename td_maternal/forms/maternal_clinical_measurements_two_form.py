from django import forms
from ..models import MaternalClinicalMeasurementsTwo
from .form_mixins import SubjectModelFormMixin
from td_maternal_validators.form_validators import MaternalClinicalMeasurememtsTwoFormValidator


class MaternalClinicalMeasurementsTwoForm(
        SubjectModelFormMixin, forms.ModelForm):
    form_validator_cls = MaternalClinicalMeasurememtsTwoFormValidator

    class Meta:
        model = MaternalClinicalMeasurementsTwo
        fields = '__all__'
