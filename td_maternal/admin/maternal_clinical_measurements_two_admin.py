from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalClinicalMeasurementsTwoForm
from ..models import MaternalClinicalMeasurementsTwo
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(MaternalClinicalMeasurementsTwo, site=td_maternal_admin)
class MaternalClinicalMeasurementsTwoAdmin(
        CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalClinicalMeasurementsTwoForm

    list_display = ('maternal_visit', 'weight_kg',
                    'systolic_bp', 'diastolic_bp')

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'weight_kg',
                'systolic_bp',
                'diastolic_bp']}
         ), audit_fieldset_tuple)
