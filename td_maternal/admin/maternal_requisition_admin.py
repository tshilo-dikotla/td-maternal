import datetime
from pytz import timezone
from django.contrib import admin
from django.http import HttpResponse
import csv

from edc_lab.admin import RequisitionAdminMixin
from edc_lab.admin import requisition_identifier_fields
from edc_lab.admin import requisition_identifier_fieldset, requisition_verify_fields
from edc_lab.admin import requisition_verify_fieldset, requisition_status_fieldset
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalRequisitionForm
from ..models import MaternalRequisition
from .modeladmin_mixins import CrfModelAdminMixin


class ExportRequisitionCsvMixin:

    def fix_date_format(self, obj_dict=None):
        """Change all dates into a format for the export
        and split the time into a separate value.
        
        Format: m/d/y
        """

        result_dict_obj = {**obj_dict}
        for key, value in obj_dict.items():
            if isinstance(value, datetime.datetime):
                value = value.astimezone(timezone('Africa/Gaborone'))
                time_value = value.time().strftime('%H:%M:%S.%f')
                time_variable = key + '_time'
                value = value.strftime('%m/%d/%Y')
                result_dict_obj[key] = value
                result_dict_obj[time_variable] = time_value
            elif isinstance(value, datetime.date):
                value = value.strftime('%m/%d/%Y')
                result_dict_obj[key] = value
        return result_dict_obj

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        field_names = self.fix_date_format(queryset[0].__dict__)
        field_names = [a for a in field_names.keys()]
        field_names += ['panel_name']
        
        writer.writerow(field_names)
        field_names.remove('panel_name')
        for obj in queryset:
            obj_data = self.fix_date_format(obj.__dict__)
            data = [obj_data[field] for field in field_names]
            data += [obj.panel.name]
            writer.writerow(data)
        return response

    export_as_csv.short_description = "Export with panel name"


@admin.register(MaternalRequisition, site=td_maternal_admin)
class MaternalRequisitionAdmin(CrfModelAdminMixin, RequisitionAdminMixin,
                               ExportRequisitionCsvMixin, admin.ModelAdmin):

    form = MaternalRequisitionForm
    actions = ["export_as_csv"]
    ordering = ('requisition_identifier',)

    fieldsets = (
        (None, {
            'fields': (
                'maternal_visit',
                'requisition_datetime',
                'is_drawn',
                'reason_not_drawn',
                'reason_not_drawn_other',
                'drawn_datetime',
                'study_site',
                'panel',
                'item_type',
                'item_count',
                'estimated_volume',
                'priority',
                'comments',
            )}),
        requisition_status_fieldset,
        requisition_identifier_fieldset,
        requisition_verify_fieldset,
        audit_fieldset_tuple)

    radio_fields = {
        'is_drawn': admin.VERTICAL,
        'reason_not_drawn': admin.VERTICAL,
        'item_type': admin.VERTICAL,
        'priority': admin.VERTICAL,
        'study_site': admin.VERTICAL,
    }

    list_display = ('maternal_visit', 'is_drawn', 'panel', 'estimated_volume',)

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj)
                +requisition_identifier_fields
                +requisition_verify_fields)
