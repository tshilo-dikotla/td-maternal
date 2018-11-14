from django.contrib import admin

from ..admin_site import td_maternal_admin
from ..forms import (MaternalClinicalMeasurementsOneForm,
                     MaternalClinicalMeasurementsTwoForm)
from ..models import (MaternalClinicalMeasurementsOne,
                      MaternalClinicalMeasurementsTwo)
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
                'maternal_visit',
                'weight_kg',
                'height',
                'systolic_bp',
                'diastolic_bp']}
         ), audit_fieldset_tuple)


@admin.register(MaternalClinicalMeasurementsTwo, site=td_maternal_admin)
class MaternalClinicalMeasurementsTwoAdmin(
        CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalClinicalMeasurementsTwoForm

    list_display = ('weight_kg', 'systolic_bp', 'diastolic_bp')
