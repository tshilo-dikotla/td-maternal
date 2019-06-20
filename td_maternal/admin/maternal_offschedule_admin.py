from django.contrib import admin

from ..admin_site import td_maternal_admin
from ..models import MaternalOffSchedule
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalOffSchedule, site=td_maternal_admin)
class MaternalOffScheduleAdmin(ModelAdminMixin, admin.ModelAdmin):

    pass
