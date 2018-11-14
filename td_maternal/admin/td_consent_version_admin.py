from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import TdConsentVersionForm
from ..models import TdConsentVersion
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(TdConsentVersion, site=td_maternal_admin)
class TdConsentVersionAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = TdConsentVersionForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_screening',
                'version',
                'report_datetime']}
         ), audit_fieldset_tuple)

    radio_fields = {'version': admin.VERTICAL}
    list_display = ('version', 'report_datetime',)
