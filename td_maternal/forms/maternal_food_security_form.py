from django import forms

from td_maternal_validators.form_validators import MaternalFoodSeccurityFormValidator

from ..models import MaternalFoodSecurity
from .form_mixins import SubjectModelFormMixin


class MaternalFoodSecurityForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalFoodSeccurityFormValidator

    class Meta:
        model = MaternalFoodSecurity
        fields = '__all__'
