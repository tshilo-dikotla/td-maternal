from td_maternal_validators.form_validators import MaternalRecontactFormValidator

from ..models import MaternalRecontact
from .form_mixins import SubjectModelFormMixin


class MaternalRecontactForm(SubjectModelFormMixin):

    form_validator_cls = MaternalRecontactFormValidator

    class Meta:
        model = MaternalRecontact
        fields = '__all__'
