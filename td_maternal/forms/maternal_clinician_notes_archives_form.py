from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import ClinicianNotesArchives, ClinicianNotesImageArchive


class ClinicianNotesArchivesForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = ClinicianNotesArchives
        fields = '__all__'


class ClinicianNotesImageArchiveForm(forms.ModelForm):

    class Meta:
        model = ClinicianNotesImageArchive
        fields = '__all__'
