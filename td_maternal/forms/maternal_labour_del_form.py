from django import forms
from td_maternal_validators.form_validators import MaternalLabDelFormValidator
from ..models import MaternalLabourDel


class MaternalLabourDelForm(forms.ModelForm):

    form_validator_cls = MaternalLabDelFormValidator

    class Meta:
        model = MaternalLabourDel
        fields = '__all__'
