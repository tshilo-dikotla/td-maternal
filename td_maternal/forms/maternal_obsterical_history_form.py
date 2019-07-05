from django import forms
from td_maternal_validators.form_validators import MaternalObstericalHistoryFormValidator
from ..models import MaternalObstericalHistory
from .form_mixins import SubjectModelFormMixin


class MaternalObstericalHistoryForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalObstericalHistoryFormValidator

    class Meta:
        model = MaternalObstericalHistory
        fields = '__all__'
