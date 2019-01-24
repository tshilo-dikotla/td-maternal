from django import forms
from td_maternal_validators.form_validators import MaternalLifetimeArvHistoryFormValidator

from ..models import MaternalLifetimeArvHistory
from .form_mixins import SubjectModelFormMixin


class MaternalLifetimeArvHistoryForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MaternalLifetimeArvHistoryFormValidator

    class Meta:
        model = MaternalLifetimeArvHistory
        fields = '__all__'
