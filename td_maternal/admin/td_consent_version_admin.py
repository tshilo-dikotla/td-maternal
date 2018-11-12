from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import TdConsentVersionForm
from ..models import TdConsentVersion
from .modeladmin_mixins import ModelAdminMixin


@admin.register(TdConsentVersion, site=td_maternal_admin)
class TdConsentVersionAdmin(admin.ModelAdmin, ModelAdminMixin):

    form = TdConsentVersionForm

    fields = ('maternal_eligibility', 'version', 'report_datetime',)
    radio_fields = {'version': admin.VERTICAL}
    list_display = ('version', 'report_datetime',)
