from django import forms
from ..models import MaternalUltraSoundFu
from .form_mixins import SubjectModelFormMixin


class MaternalUltraSoundFuForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalUltraSoundFu
        fields = '__all__'
