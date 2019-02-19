from django import forms
from td_maternal_validators.form_validators import (
    MaternalTuberculosisHistoryFormValidator
)

from ..models import KaraboTuberculosisHistory
from .form_mixins import SubjectModelFormMixin


class KaraboTuberculosisHistoryForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalTuberculosisHistoryFormValidator

    class Meta:
        model = KaraboTuberculosisHistory
        fields = '__all__'
