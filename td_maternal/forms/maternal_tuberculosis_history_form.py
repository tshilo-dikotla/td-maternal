

from django import forms
from ..models import MaternalTuberculosisHistory
# from td_maternal_validators.form_validators import (
#     MaternalTuberculosisHistoryFormValidator
# )
from .form_mixins import SubjectModelFormMixin


class MaternalTuberculosisHistoryForm(SubjectModelFormMixin, forms.ModelForm):

    #     form_validator_cls = MaternalTuberculosisHistoryFormValidator

    class Meta:
        model = MaternalTuberculosisHistory
        fields = '__all__'
