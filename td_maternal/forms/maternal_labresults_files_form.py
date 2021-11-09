from django import forms

from ..models import MaternalLabResultsFiles, LabResultsFile
from .form_mixins import InlineSubjectModelFormMixin
from .form_mixins import SubjectModelFormMixin


class MaternalLabResultsFilesForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalLabResultsFiles
        fields = '__all__'


class LabResultsFileForm(InlineSubjectModelFormMixin):

    class Meta:
        model = LabResultsFile
        fields = '__all__'
