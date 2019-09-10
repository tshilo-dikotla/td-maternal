from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalOffScheduleForm
from ..models import MaternalOffSchedule
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalOffSchedule, site=td_maternal_admin)
class MaternalOffScheduleAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalOffScheduleForm

    fieldsets = (
        (None, {
            'fields': [
                'schedule_name',
                'subject_identifier'
            ]}
         ), audit_fieldset_tuple)

    list_filter = ('schedule_name', 'subject_identifier',)
