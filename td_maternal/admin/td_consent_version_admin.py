from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_maternal_admin
from ..forms import TdConsentVersionForm
from ..models import TdConsentVersion
# from td_maternal.models.model_mixins.crf_model_mixin import CrfModelMixin
from td_maternal.admin.modeladmin_mixins import ModelAdminMixin


@admin.register(TdConsentVersion, site=td_maternal_admin)
class TdConsentVersionAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = TdConsentVersionForm
#     search_fields = ['subject_identifier']

    fieldsets = (
        (None, {
            'fields': [
                'subjectscreening',
                'report_datetime',
                'version']}
         ), audit_fieldset_tuple)

    radio_fields = {'version': admin.VERTICAL}
    list_display = ('subject_identifier', 'version',)
