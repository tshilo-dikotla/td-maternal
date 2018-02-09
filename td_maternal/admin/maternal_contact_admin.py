from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..models import MaternalContact
from ..forms import MaternalContactForm


@admin.register(MaternalContact, site=td_maternal_admin)
class MaternalContactAdmin(admin.ModelAdmin):

    form = MaternalContactForm

    fields = [
        'registered_subject',
        'report_datetime',
        'contact_type',
        'contact_datetime',
        'call_reason',
        'call_reason_other',
        'contact_success',
        'contact_comment']

    list_display = [
        'registered_subject', 'contact_type',
        'contact_datetime', 'call_reason', 'contact_success']

    list_filter = ['contact_type', 'call_reason', 'contact_success']

    radio_fields = {
        'contact_type': admin.VERTICAL,
        'call_reason': admin.VERTICAL,
        'contact_success': admin.VERTICAL
    }
