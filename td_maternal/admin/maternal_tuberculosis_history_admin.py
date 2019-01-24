from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalTuberculosisHistoryForm
from ..models import MaternalTuberculosisHistory
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalTuberculosisHistory, site=td_maternal_admin)
class MaternalTuberculosisHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = MaternalTuberculosisHistoryForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'coughing',
                'coughing_relation',
                'other_coughing_relation',
                'diagnosis',
                'diagnosis_relation',
                'other_diagnosis_relation',
                'tuberculosis_treatment',
                'tuberculosis_treatment_relation',
                'other_treatment_relation'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'coughing': admin.VERTICAL,
        'coughing_relation': admin.VERTICAL,
        'diagnosis': admin.VERTICAL,
        'diagnosis_relation': admin.VERTICAL,
        'tuberculosis_treatment': admin.VERTICAL,
        'tuberculosis_treatment_relation': admin.VERTICAL
    }

    list_display = (
        'other_coughing_relation',
        'other_diagnosis_relation',
        'other_treatment_relation')
