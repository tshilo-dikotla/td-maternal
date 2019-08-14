from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalClinicalMeasurementsOneForm
from ..models import MaternalClinicalMeasurementsOne
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(MaternalClinicalMeasurementsOne, site=td_maternal_admin)
class MaternalClinicalMeasurementsOneAdmin(
        CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalClinicalMeasurementsOneForm

    list_display = ('maternal_visit', 'weight_kg', 'height',
                    'systolic_bp', 'diastolic_bp')

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'weight_kg',
                'systolic_bp',
                'diastolic_bp',
                'height']}
         ), audit_fieldset_tuple)
