from django import forms
from edc_lab.forms.modelform_mixins import RequisitionFormMixin

from ..models import MaternalRequisition
from .form_mixins import SubjectModelFormMixin, FormValidatorMixin


class MaternalRequisitionForm(SubjectModelFormMixin, RequisitionFormMixin, FormValidatorMixin):

    requisition_identifier = forms.CharField(
        label='Requisition identifier'
    )

    class Meta:
        model = MaternalRequisition
        fields = '__all__'
