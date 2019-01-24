from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from td_maternal_validators.form_validators import MaternalLabDelFormValidator
from ..models import MaternalLabourDel


class MaternalLabourDelForm(SiteModelFormMixin, FormValidatorMixin,
                            forms.ModelForm):

    form_validator_cls = MaternalLabDelFormValidator

    class Meta:
        model = MaternalLabourDel
        fields = '__all__'
