from django import forms
from ..models import MaternalClinicalMeasurementsOne, MaternalClinicalMeasurementsTwo
from .form_mixins import SubjectModelFormMixin


class MaternalClinicalMeasurementsOneForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalClinicalMeasurementsOne
        fields = '__all__'


class MaternalClinicalMeasurementsTwoForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalClinicalMeasurementsTwo
        fields = '__all__'
