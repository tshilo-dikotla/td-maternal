from django import forms

from td_maternal_validators.form_validators import TDCRFFormValidator

from ..models import MaternalPostPartumDep
from .form_mixins import SubjectModelFormMixin


class MaternalPostPartumDepForm(SubjectModelFormMixin, TDCRFFormValidator,
                                forms.ModelForm):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'maternal_visit').subject_identifier
        self.validate_offstudy_model()

    class Meta:
        model = MaternalPostPartumDep
        fields = '__all__'
