from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalLifetimeArvHistoryForm
from ..models import MaternalLifetimeArvHistory
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(MaternalLifetimeArvHistory, site=td_maternal_admin)
class MaternalLifetimeArvHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = MaternalLifetimeArvHistoryForm

    list_filter = ('preg_on_haart',)

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'prev_preg_azt',
                'prev_sdnvp_labour',
                'prev_preg_haart',
                'haart_start_date',
                'is_date_estimated',
                'preg_on_haart',
                'haart_changes',
                'prior_preg',
                'prior_arv',
                'prior_arv_other']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'prev_preg_azt': admin.VERTICAL,
        'prev_sdnvp_labour': admin.VERTICAL,
        'prev_preg_haart': admin.VERTICAL,
        'preg_on_haart': admin.VERTICAL,
        'prior_preg': admin.VERTICAL,
        'is_date_estimated': admin.VERTICAL}

    filter_horizontal = ('prior_arv',)
