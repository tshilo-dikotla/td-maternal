from td_maternal.admin.modeladmin_mixins import ModelAdminMixin

from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import TdConsentVersionForm
from ..models import TdConsentVersion


@admin.register(TdConsentVersion, site=td_maternal_admin)
class TdConsentVersionAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = TdConsentVersionForm

    fieldsets = (
        (None, {
            'fields': [
                'screening_identifier',
                'report_datetime',
                'version']}
         ), audit_fieldset_tuple)

    radio_fields = {'version': admin.VERTICAL}
#     readonly_fields = ('screening_identifier', 'subject_identifier')
    list_display = ('version',)
