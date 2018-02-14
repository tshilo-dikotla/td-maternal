from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from edc_visit_tracking.form_validators import VisitFormValidator

from ..models import MaternalVisit


class MaternalVisitForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = VisitFormValidator

    class Meta:
        model = MaternalVisit
        fields = '__all__'
