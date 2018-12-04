from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalLocatorForm
from ..models import MaternalLocator
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalLocator, site=td_maternal_admin)
class MaternalLocatorAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalLocatorForm
