from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from edc_lab.admin import (
    RequisitionAdminMixin,
    requisition_fieldset,
    requisition_status_fieldset,
    requisition_identifier_fields,
    requisition_identifier_fieldset,
    requisition_verify_fields,
    requisition_verify_fieldset)

from ..admin_site import td_maternal_admin
from ..forms import MaternalRequisitionForm
from ..models import MaternalRequisition
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(MaternalRequisition, site=td_maternal_admin)
class MaternalRequisitionAdmin(CrfModelAdminMixin, RequisitionAdminMixin,
                               admin.ModelAdmin):

    form = MaternalRequisitionForm

    ordering = ('requisition_identifier', )

    fieldsets = (
        (None, {
            'fields': (
                'maternal_visit',
                'requisition_datetime',
                'panel',
            )}),
        requisition_fieldset,
        requisition_status_fieldset,
        requisition_identifier_fieldset,
        requisition_verify_fieldset,
        audit_fieldset_tuple)

    radio_fields = {
        'is_drawn': admin.VERTICAL,
        'reason_not_drawn': admin.VERTICAL,
        'item_type': admin.VERTICAL,
    }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj)
                + requisition_identifier_fields
                + requisition_verify_fields)
