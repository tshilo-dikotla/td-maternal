import datetime
import uuid

from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import xlwt


class ExportActionMixin:

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

        field_names = queryset[0].__dict__
        field_names = [a for a in field_names.keys()]
        field_names.remove('_state')
        if getattr(queryset[0], 'maternal_visit', None):
            field_names[:0] = ['subject_identifier', 'consent_datetime', 'visit_code']

        for col_num in range(len(field_names)):
            ws.write(row_num, col_num, field_names[col_num], font_style)

        for obj in queryset:
            obj_data = obj.__dict__
            obj_data['subject_identifier'] = obj.subject_identifier
            obj_data['consent_datetime'] = self.get_consent_datetime(obj)
            obj_data['visit_code'] = obj.maternal_visit.visit_code
            data = [obj_data[field] for field in field_names]

            row_num += 1
            for col_num in range(len(data)):
                if isinstance(data[col_num], uuid.UUID):
                    ws.write(row_num, col_num, str(data[col_num]))
                elif isinstance(data[col_num], datetime.datetime):
                    data[col_num] = timezone.make_naive(data[col_num])
                    ws.write(row_num, col_num, data[col_num], xlwt.easyxf(
                        num_format_str='YYYY/MM/DD h:mm:ss'))
                else:
                    ws.write(row_num, col_num, data[col_num])
        wb.save(response)
        return response

    export_as_csv.short_description = _(
        'Export selected %(verbose_name_plural)s')

    actions = [export_as_csv]

    def get_export_filename(self):
        date_str = datetime.datetime.now().strftime('%Y-%m-%d')
        filename = "%s-%s" % (self.model.__name__, date_str)
        return filename

    def get_consent_datetime(self, model_obj):
        subject_consent_cls = django_apps.get_model(
            'td_maternal.subjectconsent')
        consent_version = getattr(model_obj, 'consent_version', None)
        if consent_version:
            try:
                maternal_consent = subject_consent_cls.objects.get(
                    subject_identifier=model_obj.subject_identifier,
                    version=consent_version)
            except subject_consent_cls.DoesNotExist:
                raise ValidationError('Missing Maternal Consent form.')
            else:
                return maternal_consent.consent_datetime
