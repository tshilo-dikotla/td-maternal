from django import forms
from ..models import MaternalClinicalMeasurementsOne

from .form_mixins import SubjectModelFormMixin


class MaternalClinicalMeasurementsOneForm(
        SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalClinicalMeasurementsOne
        fields = '__all__'
