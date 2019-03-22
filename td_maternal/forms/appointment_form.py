from django import forms
from edc_appointment.models.appointment import Appointment
from edc_base.sites.forms import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from td_maternal_validators.form_validators import AppointmentFormValidator


class AppointmentForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):
    """Note, the appointment is only changed, never added,
    through this form.
    """

    form_validator_cls = AppointmentFormValidator

    class Meta:
        model = Appointment
        fields = '__all__'
