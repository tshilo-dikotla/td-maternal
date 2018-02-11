from django.contrib import admin
from copy import copy
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin_site import td_maternal_admin
from ..forms import MaternalVisitForm
from ..models import MaternalVisit
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalVisit, site=td_maternal_admin)
class MaternalVisitAdmin(VisitModelAdminMixin, ModelAdminMixin, admin.ModelAdmin):

    form = MaternalVisitForm

    def get_fieldsets(self, request, obj=None):
        fields = copy(self.fields)
        fields.remove('information_provider')
        fields.remove('information_provider_other')
        return [(None, {'fields': fields})]
