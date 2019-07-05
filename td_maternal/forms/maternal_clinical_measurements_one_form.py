from django import forms
from td_maternal_validators.form_validators import MaternalClinicalMeasurememtsOneFormValidator

from ..models import MaternalClinicalMeasurementsOne
from .form_mixins import SubjectModelFormMixin


class MaternalClinicalMeasurementsOneForm(
        SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalClinicalMeasurememtsOneFormValidator

    class Meta:
        model = MaternalClinicalMeasurementsOne
        fields = '__all__'
