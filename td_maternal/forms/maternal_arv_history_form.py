from django import forms

from ..models import MaternalLifetimeArvHistory
from .form_mixins import SubjectModelFormMixin


class MaternalLifetimeArvHistoryForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalLifetimeArvHistory
        fields = '__all__'
