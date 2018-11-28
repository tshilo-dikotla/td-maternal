from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalDiagnosesForm
from ..models import MaternalDiagnoses
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalDiagnoses, site=td_maternal_admin)
class MaternalDiagnosesAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalDiagnosesForm
    list_display = ('maternal_visit', 'new_diagnoses', 'has_who_dx')
    list_filter = ('new_diagnoses', 'has_who_dx')
    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'maternal_visit',
                'new_diagnoses',
                'diagnoses',
                'diagnoses_other',
                'has_who_dx',
                'who']}
         ), audit_fieldset_tuple)

    radio_fields = {'new_diagnoses': admin.VERTICAL,
                    'has_who_dx': admin.VERTICAL}
    filter_horizontal = ('who', 'diagnoses')
