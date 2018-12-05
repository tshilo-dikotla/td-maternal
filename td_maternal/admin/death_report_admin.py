from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_maternal_admin
from ..forms import DeathReportForm
from ..models import DeathReport
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(DeathReport, site=td_maternal_admin)
class DeathReportAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = DeathReportForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'death_date',
                'primary_source',
                'primary_source_other',
                'perform_autopsy',
                'narrative',
                'cause_category',
                'cause_category_other',
                'cause_of_death',
                'cause_of_death_other',
                'illness_duration',
                'medical_responsibility',
                'participant_hospitalized',
                'reason_hospitalized',
                'reason_hospitalized_other',
                'days_hospitalized',
                'comment', ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'cause_of_death': admin.VERTICAL,
        'primary_source': admin.VERTICAL,
        'cause_of_death': admin.VERTICAL,
        'cause_category': admin.VERTICAL,
        'perform_autopsy': admin.VERTICAL,
        'medical_responsibility': admin.VERTICAL,
        'participant_hospitalized': admin.VERTICAL,
        'reason_hospitalized': admin.VERTICAL}