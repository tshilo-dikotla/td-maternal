from copy import copy
from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin_site import td_maternal_admin
from ..forms import MaternalVisitForm
from ..models import MaternalVisit
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalVisit, site=td_maternal_admin)
class MaternalVisitAdmin(ModelAdminMixin,
                         VisitModelAdminMixin, admin.ModelAdmin):

    visit_attr = 'maternal_visit'
    dashboard_type = 'maternal'

    form = MaternalVisitForm

    fieldsets = (
        (None, {
            'fields': [
                'appointment',
                'report_datetime',
                'reason',
                'reason_unscheduled',
                'reason_unscheduled_other',
                'info_source',
                'info_source_other',
                'comments'
            ]}),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple
    )

    radio_fields = {
        'reason': admin.VERTICAL,
        'reason_unscheduled': admin.VERTICAL,
        'info_source': admin.VERTICAL}

#     def get_fieldsets(self, request, obj=None):
#         fields = copy(self.fields)
#         fields.remove('information_provider')
#         fields.remove('information_provider_other')
#         return [(None, {'fields': fields})]
