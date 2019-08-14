from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, audit_fields

from ..admin_site import td_maternal_admin
from ..forms import KaraboSubjectScreeningForm
from ..models import KaraboSubjectScreening
from .modeladmin_mixins import ModelAdminMixin


@admin.register(KaraboSubjectScreening, site=td_maternal_admin)
class KaraboSubjectScreeningAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = KaraboSubjectScreeningForm

    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'screening_identifier',
                'subject_identifier',
                'infant_alive',
                'infant_weight',
                'major_anomalies',
                'birth_complications',
                'infant_documentation',
                'infant_months',
                'tb_treatment',
                'incarcerated',
                'willing_to_consent'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'infant_alive': admin.VERTICAL,
        'infant_weight': admin.VERTICAL,
        'major_anomalies': admin.VERTICAL,
        'birth_complications': admin.VERTICAL,
        'infant_documentation': admin.VERTICAL,
        'infant_months': admin.VERTICAL,
        'tb_treatment': admin.VERTICAL,
        'incarcerated': admin.VERTICAL,
        'willing_to_consent': admin.VERTICAL,
    }

    list_display = ('screening_identifier',
                    'subject_identifier',
                    'infant_alive',
                    'willing_to_consent')

    readonly_fields = ('screening_identifier',)

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                +audit_fields)
