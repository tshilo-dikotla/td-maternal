from django.contrib import admin

from edc_model_admin import ModelAdminNextUrlRedirectMixin
from ..admin_site import td_maternal_admin
from ..forms import MaternalEligibilityForm
from ..models import MaternalEligibility
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalEligibility, site=td_maternal_admin)
class MaternalEligibilityAdmin(ModelAdminNextUrlRedirectMixin, admin.ModelAdmin):

    form = MaternalEligibilityForm

    fields = ('eligibility_id',
              'report_datetime',
              'age_in_years',
              'has_omang')

    radio_fields = {'has_omang': admin.VERTICAL}

    readonly_fields = ('eligibility_id',)

    list_display = (
        'report_datetime', 'age_in_years', 'is_eligible', 'is_consented')

    list_filter = ('report_datetime', 'is_eligible', 'is_consented')
