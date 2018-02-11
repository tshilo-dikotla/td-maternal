from django import forms
from ..models import MaternalObstericalHistory
from .form_mixins import SubjectModelFormMixin


class MaternalObstericalHistoryForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalObstericalHistory
        fields = '__all__'
