from django import forms

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from td_maternal_validators.form_validators import AntenatalEnrollmentFormValidator

from ..models import AntenatalEnrollment


class AntenatalEnrollmentForm(
        SiteModelFormMixin, FormValidatorMixin,
        forms.ModelForm):

    form_validator_cls = AntenatalEnrollmentFormValidator

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = AntenatalEnrollment
        fields = '__all__'
