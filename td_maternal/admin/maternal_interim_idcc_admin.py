from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalInterimIdccForm
from ..models import MaternalInterimIdcc
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalInterimIdcc, site=td_maternal_admin)
class MaternalInterimIdccAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalInterimIdccForm

    list_display = ('report_datetime', 'recent_cd4', 'value_vl',)

    list_filter = (
        'info_since_lastvisit', 'recent_cd4_date',
        'value_vl_size', 'recent_vl_date')

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'info_since_lastvisit',
                'recent_cd4',
                'recent_cd4_date',
                'value_vl_size',
                'value_vl',
                'recent_vl_date',
                'other_diagnoses']}
         ), audit_fieldset_tuple)

    radio_fields = {'info_since_lastvisit': admin.VERTICAL,
                    'value_vl_size': admin.VERTICAL}
