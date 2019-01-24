from django import forms
from td_maternal_validators.form_validators import MaternalIterimIdccFormValidator
from ..models import MaternalInterimIdcc
from .form_mixins import SubjectModelFormMixin


class MaternalInterimIdccForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalIterimIdccFormValidator

    class Meta:
        model = MaternalInterimIdcc
        fields = '__all__'
