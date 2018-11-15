from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalPostPartumFuForm
from ..models import MaternalPostPartumFu
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalPostPartumFu, site=td_maternal_admin)
class MaternalPostPartumFuAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalPostPartumFuForm
    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'hospitalized',
                'hospitalization_reason',
                'hospitalization_reason_other',
                'hospitalization_days']}
         ), audit_fieldset_tuple)

    list_display = ('maternal_visit', 'new_diagnoses', 'has_who_dx')
    list_filter = ('new_diagnoses', 'diagnoses', 'has_who_dx')
    radio_fields = {'new_diagnoses': admin.VERTICAL,
                    'hospitalized': admin.VERTICAL,
                    'has_who_dx': admin.VERTICAL}
    filter_horizontal = ('who', 'diagnoses', 'hospitalization_reason')
