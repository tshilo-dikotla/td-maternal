import csv
import datetime
from pytz import timezone
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _


class ExportActionMixin:

    def fix_date_format(self, obj_dict=None):
        """Change all datetime into a format for the export

        Format: m-d-y H:m:s
        """

        result_dict_obj = {**obj_dict}
        for key, value in obj_dict.items():
            if isinstance(value, datetime.datetime):
                value = value.astimezone(timezone('Africa/Gaborone'))
                value = value.strftime('%Y-%m-%d %H:%M:%S')
                result_dict_obj[key] = value
            elif isinstance(value, datetime.date):
                value = value.strftime('%Y-%m-%d')
                result_dict_obj[key] = value
        return result_dict_obj

    def export_as_csv(self, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % (
            self.get_export_filename())
        writer = csv.writer(response)

        field_names = self.fix_date_format(queryset[0].__dict__)
        field_names = [a for a in field_names.keys()]
        field_names.remove('_state')
        writer.writerow(field_names)
        for obj in queryset:
            obj_data = self.fix_date_format(obj.__dict__)
            data = [obj_data[field] for field in field_names]
            writer.writerow(data)
        return response

    export_as_csv.short_description = _(
        'Export selected %(verbose_name_plural)s')

    actions = [export_as_csv]

    def get_export_filename(self):
        date_str = datetime.datetime.now().strftime('%Y-%m-%d')
        filename = "%s-%s" % (self.model.__name__, date_str)
        return filename
