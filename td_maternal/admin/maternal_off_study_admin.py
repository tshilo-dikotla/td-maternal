from django.contrib import admin
from django.conf import settings

from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_metadata import NextFormGetter
from edc_subject_dashboard import ModelAdminSubjectDashboardMixin
from edc_base.sites.admin import ModelAdminSiteMixin

from ..admin_site import td_maternal_admin
from ..models import MaternalOffStudy
from ..forms import MaternalOffStudyForm


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin, ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSubjectDashboardMixin, ModelAdminSiteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    next_form_getter_cls = NextFormGetter
    subject_dashboard_url = 'subject_dashboard_url'

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        subject_dashboard_url)

    def post_url_on_delete_kwargs(self, request, obj):
        return dict(subject_identifier=obj.subject_identifier)


@admin.register(MaternalOffStudy, site=td_maternal_admin)
class MaternalOffStudyAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalOffStudyForm
