from django import forms
from ..models import MaternalPostPartumFu
from .form_mixins import SubjectModelFormMixin


class MaternalPostPartumFuForm(SubjectModelFormMixin, forms.ModelForm):

    total_score = forms.CharField(
        label='Total score',
        required=False,
        widget=forms.TextInput(attrs={'read_only': 'read_only'}))

    class Meta:
        model = MaternalPostPartumFu
        fields = '__all__'
