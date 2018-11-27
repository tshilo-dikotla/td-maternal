from django.contrib import admin

from ..admin_site import td_maternal_admin
from ..forms import MaternalClinicalMeasurementsTwoForm
from ..models import MaternalClinicalMeasurementsTwo
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalClinicalMeasurementsTwo, site=td_maternal_admin)
class MaternalClinicalMeasurementsTwoAdmin(
        CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalClinicalMeasurementsTwoForm

    list_display = ('weight_kg', 'systolic_bp', 'diastolic_bp')

    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'maternal_visit',
                'weight_kg',
                'systolic_bp',
                'diastolic_bp']}
         ), audit_fieldset_tuple)
