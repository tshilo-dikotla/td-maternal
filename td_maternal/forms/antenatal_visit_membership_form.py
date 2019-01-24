from django import forms

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from ..models import AntenatalVisitMembership


class AntenatalVisitMembershipForm(
        SiteModelFormMixin, FormValidatorMixin,
        forms.ModelForm):

    class Meta:
        model = AntenatalVisitMembership
        fields = '__all__'
