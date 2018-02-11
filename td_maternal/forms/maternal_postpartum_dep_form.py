from django import forms
from ..models import MaternalPostPartumDep
from .form_mixins import SubjectModelFormMixin


class MaternalPostPartumDepForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalPostPartumDep
        fields = '__all__'
