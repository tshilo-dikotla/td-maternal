from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import MaternalLabResultsFiles, LabResultsFile


class MaternalLabResultsFilesForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = MaternalLabResultsFiles
        fields = '__all__'


class LabResultsFileForm(forms.ModelForm):

    class Meta:
        model = LabResultsFile
        fields = '__all__'
