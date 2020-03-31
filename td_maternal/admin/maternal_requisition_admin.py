import datetime
import uuid

from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone
from edc_lab.admin import RequisitionAdminMixin
from edc_lab.admin import requisition_identifier_fields
from edc_lab.admin import requisition_identifier_fieldset, requisition_verify_fields
from edc_lab.admin import requisition_verify_fieldset, requisition_status_fieldset
from edc_model_admin import audit_fieldset_tuple
import xlwt

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
                value = timezone.make_naive(value)
                time_value = value.time()
                time_variable = key + '_time'
                result_dict_obj[key] = value.date()
                result_dict_obj[time_variable] = time_value
        return result_dict_obj

    def export_as_csv(self, request, queryset):

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=%s.xls' % (
            self.get_export_filename())

        wb = xlwt.Workbook(encoding='utf-8', style_compression=2)
        ws = wb.add_sheet('%s')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        font_style.num_format_str = 'YYYY/MM/DD h:mm:ss'

        field_names = self.fix_date_format(queryset[0].__dict__)
        field_names = [a for a in field_names.keys()]
        field_names += ['panel_name']
        field_names.remove('_state')

        for col_num in range(len(field_names)):
            ws.write(row_num, col_num, field_names[col_num], font_style)

        field_names.remove('panel_name')
        for obj in queryset:
            obj_data = self.fix_date_format(obj.__dict__)
            data = [obj_data[field] for field in field_names]
            data += [obj.panel.name]

            row_num += 1
            for col_num in range(len(data)):
                if isinstance(data[col_num], uuid.UUID):
                    ws.write(row_num, col_num, str(data[col_num]))
                elif isinstance(data[col_num], datetime.date):
                    ws.write(row_num, col_num, data[col_num], xlwt.easyxf(num_format_str='YYYY/MM/DD'))
                elif isinstance(data[col_num], datetime.time):
                    ws.write(row_num, col_num, data[col_num], xlwt.easyxf(num_format_str='h:mm:ss'))
                else:
                    ws.write(row_num, col_num, data[col_num])
        wb.save(response)
        return response

    export_as_csv.short_description = "Export with panel name"


@admin.register(MaternalRequisition, site=td_maternal_admin)
class MaternalRequisitionAdmin(ExportRequisitionCsvMixin, CrfModelAdminMixin,
                               RequisitionAdminMixin, admin.ModelAdmin):

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
