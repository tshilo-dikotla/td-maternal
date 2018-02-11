from django import forms
from ..models import MaternalRando
from .form_mixins import SubjectModelFormMixin


class MaternalRandomizationForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalRando
        fields = '__all__'
