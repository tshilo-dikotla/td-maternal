from django import forms
from edc_form_validators import FormValidatorMixin
from td_maternal_validators.form_validators import MaternalContactFormValidator

from ..models import MaternalContact


class MaternalContactForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = MaternalContactFormValidator

    class Meta:
        model = MaternalContact
        fields = '__all__'
