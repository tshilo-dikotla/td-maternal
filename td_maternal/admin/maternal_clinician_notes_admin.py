from django.contrib import admin
from edc_model_admin import TabularInlineMixin, audit_fields

from ..admin_site import td_maternal_admin
from ..forms import ClinicianNotesForm, ClinicianNotesImageForm
from ..models import ClinicianNotes, ClinicianNotesImage
from .modeladmin_mixins import CrfModelAdminMixin


class ClinicianNotesImageInline(TabularInlineMixin, admin.TabularInline):

    model = ClinicianNotesImage
    form = ClinicianNotesImageForm
    extra = 0

    fields = ('clinician_notes_image', 'user_uploaded', 'datetime_captured',
              'modified', 'hostname_created',)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = (
            'clinician_notes_image', 'datetime_captured', 'user_uploaded') + fields

        return fields


@admin.register(ClinicianNotes, site=td_maternal_admin)
class ClinicianNotesAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = ClinicianNotesForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
            ]}
         ),)

    inlines = [ClinicianNotesImageInline]
