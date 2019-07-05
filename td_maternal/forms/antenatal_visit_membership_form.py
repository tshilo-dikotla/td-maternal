from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from td_maternal_validators.form_validators import AntenatalVisitMembershipFormValidator

from ..models import AntenatalVisitMembership


class AntenatalVisitMembershipForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = AntenatalVisitMembershipFormValidator

    class Meta:
        model = AntenatalVisitMembership
        fields = '__all__'
