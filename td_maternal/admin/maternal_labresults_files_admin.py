from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_odk.admin import StampImageActionMixin

from ..admin_site import td_maternal_admin
from ..forms import MaternalLabResultsFilesForm, LabResultsFileForm
from ..models import MaternalLabResultsFiles, LabResultsFile
from .modeladmin_mixins import CrfModelAdminMixin


class LabResultsFileInline(TabularInlineMixin, admin.TabularInline):

    model = LabResultsFile
    form = LabResultsFileForm
    extra = 0

    fields = ('lab_results_preview', 'image', 'user_uploaded', 'datetime_captured',
              'modified', 'hostname_created',)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = (
            'lab_results_preview', 'datetime_captured', 'user_uploaded') + fields

        return fields


@admin.register(MaternalLabResultsFiles, site=td_maternal_admin)
class MaternalLabResultsFilesAdmin(
        StampImageActionMixin, CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalLabResultsFilesForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
            ]}
         ), )

    inlines = [LabResultsFileInline]
