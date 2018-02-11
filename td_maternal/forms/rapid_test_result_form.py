from django import forms
from ..models import RapidTestResult
from .form_mixins import SubjectModelFormMixin


class RapidTestResultForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = RapidTestResult
        fields = '__all__'
