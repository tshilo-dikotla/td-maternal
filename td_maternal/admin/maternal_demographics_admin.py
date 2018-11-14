from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalDemographicsForm
from ..models import MaternalDemographics
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalDemographics, site=td_maternal_admin)
class MaternalDemographicsAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalDemographicsForm

    list_display = ('maternal_visit',
                    'marital_status',
                    'ethnicity',
                    'highest_education',
                    'own_phone')
    list_filter = ('marital_status',
                   'ethnicity',
                   'highest_education',
                   'own_phone')

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'marital_status',
                'ethnicity',
                'highest_education',
                'current_occupation',
                'provides_money',
                'money_earned',
                'own_phone',
                'water_source',
                'house_electrified',
                'house_fridge',
                'cooking_method',
                'toilet_facility',
                'house_type']}
         ), audit_fieldset_tuple)

    radio_fields = {'marital_status': admin.VERTICAL,
                    'ethnicity': admin.VERTICAL,
                    'highest_education': admin.VERTICAL,
                    'current_occupation': admin.VERTICAL,
                    'provides_money': admin.VERTICAL,
                    'money_earned': admin.VERTICAL,
                    'own_phone': admin.VERTICAL,
                    'water_source': admin.VERTICAL,
                    'house_electrified': admin.VERTICAL,
                    'house_fridge': admin.VERTICAL,
                    'cooking_method': admin.VERTICAL,
                    'toilet_facility': admin.VERTICAL,
                    'house_type': admin.VERTICAL}
