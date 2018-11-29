from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalSubstanceUseDuringPregForm
from ..models import MaternalSubstanceUseDuringPreg
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalSubstanceUseDuringPreg, site=td_maternal_admin)
class MaternalSubstanceUseDuringPregAdmin(
        CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalSubstanceUseDuringPregForm

    list_display = (
        'smoked_during_pregnancy',
        'smoking_during_preg_freq',
        'alcohol_during_pregnancy',
        'alcohol_during_preg_freq',
        'marijuana_during_preg',
        'marijuana_during_preg_freq',
    )

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'smoked_during_pregnancy',
                'smoking_during_preg_freq',
                'alcohol_during_pregnancy',
                'alcohol_during_preg_freq',
                'marijuana_during_preg',
                'marijuana_during_preg_freq',
                'other_illicit_substances_during_preg']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'smoked_during_pregnancy': admin.VERTICAL,
        'smoking_during_preg_freq': admin.VERTICAL,
        'alcohol_during_pregnancy': admin.VERTICAL,
        'alcohol_during_preg_freq': admin.VERTICAL,
        'marijuana_during_preg': admin.VERTICAL,
        'marijuana_during_preg_freq': admin.VERTICAL}
