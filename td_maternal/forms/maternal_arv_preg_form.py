from django import forms
from ..models import MaternalArvPreg, MaternalArv
from .form_mixins import SubjectModelFormMixin


class MaternalArvPregForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalArvPreg
        fields = '__all__'


class MaternalArvForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalArv
        fields = '__all__'
