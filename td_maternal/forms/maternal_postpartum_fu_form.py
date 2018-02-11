from django import forms
from ..models import MaternalPostPartumFu
from .form_mixins import SubjectModelFormMixin


class MaternalPostPartumFuForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalPostPartumFu
        fields = '__all__'
