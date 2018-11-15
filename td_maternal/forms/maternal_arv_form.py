from django import forms
from ..models import MaternalArv
from .form_mixins import SubjectModelFormMixin


class MaternalArvForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalArv
        fields = '__all__'
