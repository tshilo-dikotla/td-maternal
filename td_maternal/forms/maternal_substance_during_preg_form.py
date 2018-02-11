from django import forms
from ..models import MaternalSubstanceUseDuringPreg
from .form_mixins import SubjectModelFormMixin


class MaternalSubstanceUseDuringPregForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalSubstanceUseDuringPreg
        fields = '__all__'
