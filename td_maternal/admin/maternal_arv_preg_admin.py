from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalArvPregForm, MaternalArvForm
from ..models import MaternalArvPreg, MaternalArv
from .modeladmin_mixins import CrfModelAdminMixin


class MaternalArvInlineAdmin(TabularInlineMixin, admin.TabularInline):
    model = MaternalArv
    form = MaternalArvForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': [
                'maternal_arv_preg',
                'arv_code',
                'start_date',
                'stop_date',
                'reason_for_stop',
                'reason_for_stop_other']}
         ), audit_fieldset_tuple)


@admin.register(MaternalArvPreg, site=td_maternal_admin)
class MaternalArvPregAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = MaternalArvPregForm
    inlines = [MaternalArvInlineAdmin, ]
    list_display = ('maternal_visit', 'took_arv', 'is_interrupt',)
    list_filter = ('took_arv',)

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'took_arv',
                'is_interrupt',
                'interrupt',
                'interrupt_other']}
         ),)

    radio_fields = {'took_arv': admin.VERTICAL,
                    'is_interrupt': admin.VERTICAL,
                    'interrupt': admin.VERTICAL
                    }
