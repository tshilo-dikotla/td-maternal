from django import forms
from ..models import MaternalContraception
from .form_mixins import SubjectModelFormMixin


class MaternalContraceptionForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalContraception
        fields = '__all__'
