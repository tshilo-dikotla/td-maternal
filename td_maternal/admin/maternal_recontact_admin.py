from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalRecontactForm
from ..models import MaternalRecontact
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalRecontact, site=td_maternal_admin)
class MaternalRecontactAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalRecontactForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'contact_date',
                'future_contact',
                'reason_no_contact'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'future_contact': admin.VERTICAL,
    }
