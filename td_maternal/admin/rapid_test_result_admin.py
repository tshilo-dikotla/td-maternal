from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import RapidTestResultForm
from ..models import RapidTestResult
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(RapidTestResult, site=td_maternal_admin)
class RapidTestResultAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = RapidTestResultForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'rapid_test_done',
                'result_date',
                'result',
                'comments']}
         ), audit_fieldset_tuple)

    list_display = ('maternal_visit',
                    'rapid_test_done',
                    'result')
    list_filter = ('rapid_test_done', 'result')
    search_fields = ('result_date', )
    radio_fields = {"rapid_test_done": admin.VERTICAL,
                    "result": admin.VERTICAL, }
