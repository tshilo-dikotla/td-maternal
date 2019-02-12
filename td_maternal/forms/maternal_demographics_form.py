from td_maternal_validators.form_validators import MaternalDemographicsFormValidator

from ..models import MaternalDemographics
from .form_mixins import SubjectModelFormMixin


class MaternalDemographicsForm(SubjectModelFormMixin):

    form_validator_cls = MaternalDemographicsFormValidator

    class Meta:
        model = MaternalDemographics
        fields = '__all__'
