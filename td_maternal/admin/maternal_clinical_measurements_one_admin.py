from django.contrib import admin

from ..admin_site import td_maternal_admin
from ..forms import MaternalClinicalMeasurementsOneForm
from ..models import MaternalClinicalMeasurementsOne
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalClinicalMeasurementsOne, site=td_maternal_admin)
class MaternalClinicalMeasurementsOneAdmin(
        CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalClinicalMeasurementsOneForm

    list_display = ('weight_kg', 'height', 'systolic_bp', 'diastolic_bp')

    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'maternal_visit',
                'weight_kg',
                'height',
                'systolic_bp',
                'diastolic_bp']}
         ), audit_fieldset_tuple)
