from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalUltraSoundInitialForm
from ..models import MaternalUltraSoundInitial
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalUltraSoundInitial, site=td_maternal_admin)
class MaternalUltraSoundInitialAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalUltraSoundInitialForm

    fieldsets = (
        (None, {
            'fields': [
                'number_of_gestations',
                'ga_by_lmp',
                'ga_by_ultrasound_wks',
                'ga_by_ultrasound_days',
                'est_fetal_weight',
                'est_edd_ultrasound',
                'edd_confirmed',
                'ga_confirmed',
                'ga_confrimation_method']}
         ), audit_fieldset_tuple)

    readonly_fields = ('edd_confirmed', 'ga_confirmed', 'ga_by_lmp')

    radio_fields = {'number_of_gestations': admin.VERTICAL,
                    'amniotic_fluid_volume': admin.VERTICAL, }

    list_display = (
        'number_of_gestations', 'ga_confrimation_method', 'edd_confirmed',
        'ga_confirmed', 'ga_by_lmp')

    list_filter = ('number_of_gestations', 'ga_confrimation_method')
