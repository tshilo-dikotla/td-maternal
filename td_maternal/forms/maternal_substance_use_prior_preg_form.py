from django import forms
from ..models import MaternalSubstanceUsePriorPreg
from .form_mixins import SubjectModelFormMixin


class MaternalSubstanceUsePriorPregForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalSubstanceUsePriorPreg
        fields = '__all__'
