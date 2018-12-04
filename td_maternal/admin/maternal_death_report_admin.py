from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_maternal_admin
from ..forms import MaternalDeathReportForm
from ..models import DeathReport
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(DeathReport, site=td_maternal_admin)
class MaternalDeathReportAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalDeathReportForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'death_datetime',
                'study_day',
                'death_as_inpatient',
                'cause_of_death',
                'cause_of_death_other',
                'tb_site',
                'narrative']}
         ), audit_fieldset_tuple)
