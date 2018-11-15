from django import forms
from ..models import MaternalArvPreg
from .form_mixins import SubjectModelFormMixin


class MaternalArvPregForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalArvPreg
        fields = '__all__'
