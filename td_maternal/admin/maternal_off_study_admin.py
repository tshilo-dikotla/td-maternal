from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..models import MaternalOffStudy
from ..forms import MaternalOffStudyForm
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(MaternalOffStudy, site=td_maternal_admin)
class MaternalOffStudyAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalOffStudyForm

    fields = (
        'maternal_visit',
        'report_datetime',
        'offstudy_date',
        'reason',
        'reason_other',
        'comment')
