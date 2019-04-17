from django import forms
from django.core.exceptions import ValidationError
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

    def clean(self):
        rapid_test_date = self.cleaned_data.get('rapid_test_date')

        if self.instance.rapid_test_date and rapid_test_date:
            if rapid_test_date != self.instance.rapid_test_date:
                raise ValidationError(
                    'The rapid test result cannot be changed')
        super().clean()

    class Meta:
        model = AntenatalEnrollment
        fields = '__all__'
