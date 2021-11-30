from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_odk.admin import StampImageActionMixin

from ..admin_site import td_maternal_admin
from ..forms import ClinicianNotesImageArchiveForm, ClinicianNotesArchivesForm
from ..models import ClinicianNotesArchives, ClinicianNotesImageArchive
from .modeladmin_mixins import ModelAdminMixin


class ClinicianNotesImageInline(TabularInlineMixin, admin.TabularInline):

    model = ClinicianNotesImageArchive
    form = ClinicianNotesImageArchiveForm
    extra = 0

    fields = ('clinician_notes_image', 'image', 'user_uploaded', 'datetime_captured',
              'modified', 'hostname_created',)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = (
            'clinician_notes_image', 'datetime_captured', 'user_uploaded') + fields

        return fields


@admin.register(ClinicianNotesArchives, site=td_maternal_admin)
class ClinicianNotesArchivesAdmin(StampImageActionMixin, ModelAdminMixin, admin.ModelAdmin):

    form = ClinicianNotesArchivesForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
            ]}
         ),)

    list_display = ('subject_identifier', 'created', )

    inlines = [ClinicianNotesImageInline]

    search_fields = ('subject_identifier',)
