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
                'fever',
                'fever_rel',
                'other_fever_rel',
                'weight_loss',
                'weight_loss_rel',
                'other_weight_loss',
                'night_sweats',
                'night_sweats_rel',
                'other_night_sweats',
                'diagnosis',
                'diagnosis_rel',
                'other_diagnosis_rel',
                'tb_exposure',
                'tb_exposure_det'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'coughing': admin.VERTICAL,
        'coughing_rel': admin.VERTICAL,
        'fever': admin.VERTICAL,
        'fever_rel': admin.VERTICAL,
        'weight_loss': admin.VERTICAL,
        'weight_loss_rel': admin.VERTICAL,
        'diagnosis': admin.VERTICAL,
        'night_sweats': admin.VERTICAL,
        'night_sweats_rel': admin.VERTICAL,
        'diagnosis': admin.VERTICAL,
        'diagnosis_rel': admin.VERTICAL,
        'tb_exposure': admin.VERTICAL,
    }

    list_display = (
        'other_coughing_rel',
        'other_diagnosis_rel',
        'other_fever_rel',
        'other_weight_loss',
        'other_night_sweats',
        'other_diagnosis_rel',
        'tb_exposure_det')
