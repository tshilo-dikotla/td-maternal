from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_maternal_admin
from ..forms import MaternalLocatorForm
from ..models import MaternalLocator
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalLocator, site=td_maternal_admin)
class MaternalLocatorAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalLocatorForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'locator_date',
                'mail_address',
                'health_care_infant',
                'may_visit_home',
                'physical_address',
                'may_call',
                'subject_cell',
                'subject_cell_alt']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'may_call': admin.VERTICAL,
        'may_visit_home': admin.VERTICAL}
