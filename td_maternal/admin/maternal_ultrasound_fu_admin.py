from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_maternal_admin
from ..forms import MaternalUltraSoundFuForm
from ..models import MaternalUltraSoundFu
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalUltraSoundFu, site=td_maternal_admin)
class MaternalUltraSoundFuAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalUltraSoundFuForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'bpd',
                'hc',
                'ac',
                'fl',
                'amniotic_fluid_volume']}
         ), audit_fieldset_tuple)

    radio_fields = {'amniotic_fluid_volume': admin.VERTICAL, }

    list_display = ('maternal_visit', 'report_datetime')

    list_filter = ('report_datetime',)
