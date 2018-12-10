from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin_site import td_maternal_admin
from ..forms import MaternalVisitForm
from ..models import MaternalVisit
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalVisit, site=td_maternal_admin)
class MaternalVisitAdmin(VisitModelAdminMixin,
                         ModelAdminMixin, admin.ModelAdmin):

    visit_attr = 'maternal_visit'
    dashboard_type = 'maternal'

    form = MaternalVisitForm

    fieldsets = (
        (None, {
            'fields': [
                'appointment',
                'report_datetime',
                'reason',
                'reason_missed',
                'study_status',
                'require_crfs',
                'info_source',
                'info_source_other',
                'is_present',
                'survival_status',
                'last_alive_date'
            ]}),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple
    )

    radio_fields = {
        'reason': admin.VERTICAL,
        'study_status': admin.VERTICAL,
        'require_crfs': admin.VERTICAL,
        'info_source': admin.VERTICAL,
        'is_present': admin.VERTICAL,
        'survival_status': admin.VERTICAL}

#     def get_fieldsets(self, request, obj=None):
#         fields = copy(self.fields)
#         fields.remove('information_provider')
#         fields.remove('information_provider_other')
#         return [(None, {'fields': fields})]
