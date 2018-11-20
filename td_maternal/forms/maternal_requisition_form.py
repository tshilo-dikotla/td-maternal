from django import forms
from .form_mixins import SubjectModelFormMixin
from edc_lab.forms.modelform_mixins import RequisitionFormMixin

from ..models import MaternalRequisition


class MaternalRequisitionForm(SubjectModelFormMixin, RequisitionFormMixin):

    requisition_identifier = forms.CharField(
        label='Requisition identifier'
    )

    class Meta:
        model = MaternalRequisition
        fields = '__all__'
