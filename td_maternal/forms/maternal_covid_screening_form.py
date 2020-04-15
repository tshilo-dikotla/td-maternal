from django import forms
from td_maternal_validators.form_validators import MaternalCovidScreeningFormValidator

from ..models import MaternalCovidScreening
from .form_mixins import SubjectModelFormMixin


class MaternalCovidScreeningForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalCovidScreeningFormValidator

    class Meta:
        model = MaternalCovidScreening
        fields = '__all__'
