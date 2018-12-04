from django import forms
from ..models import TdConsentVersion
from td_maternal.forms.form_mixins import SubjectModelFormMixin


class TdConsentVersionForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = TdConsentVersion
        fields = '__all__'
