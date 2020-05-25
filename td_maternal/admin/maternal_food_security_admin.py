from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalFoodSecurityForm
from ..models import MaternalFoodSecurity
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(MaternalFoodSecurity, site=td_maternal_admin)
class MaternalFoodSecurityAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = MaternalFoodSecurityForm

    list_filter = ('food_sufficient',)

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'food_sufficient',
                'balanced_meal',
                'skip_meals',
                'skip_meals_frequency',
                'eat_less',
                'hungry',
                'food_basket',
                'additional_comments']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'food_sufficient': admin.VERTICAL,
        'balanced_meal': admin.VERTICAL,
        'skip_meals': admin.VERTICAL,
        'eat_less': admin.VERTICAL,
        'hungry': admin.VERTICAL,
        'food_basket': admin.VERTICAL}
