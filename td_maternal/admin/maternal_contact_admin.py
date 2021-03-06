from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalContactForm
from ..models import MaternalContact
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalContact, site=td_maternal_admin)
class MaternalContactAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalContactForm

    search_fields = ['subject_identifier']

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'contact_type',
                'contact_datetime',
                'call_reason',
                'call_reason_other',
                'contact_success',
                'contact_comment']}
         ), audit_fieldset_tuple)

    list_display = [
        'subject_identifier', 'contact_type',
        'contact_datetime', 'call_reason', 'contact_success']

    list_filter = ['contact_type', 'call_reason', 'contact_success']

    radio_fields = {
        'contact_type': admin.VERTICAL,
        'call_reason': admin.VERTICAL,
        'contact_success': admin.VERTICAL
    }
