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
                'coughing_rel',
                'other_coughing_rel',
                'diagnosis',
                'diagnosis_rel',
                'other_diagnosis_rel',
                'tb_treatment',
                'tb_treatment_rel',
                'other_treatment_rel'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'coughing': admin.VERTICAL,
        'coughing_rel': admin.VERTICAL,
        'diagnosis': admin.VERTICAL,
        'diagnosis_rel': admin.VERTICAL,
        'tb_treatment': admin.VERTICAL,
        'tb_treatment_rel': admin.VERTICAL
    }

    list_display = (
        'other_coughing_rel',
        'other_diagnosis_rel',
        'other_treatment_rel')
