from django import forms
from ..models import MaternalClinicalMeasurementsTwo
from .form_mixins import SubjectModelFormMixin


class MaternalClinicalMeasurementsTwoForm(
        SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalClinicalMeasurementsTwo
        fields = '__all__'
