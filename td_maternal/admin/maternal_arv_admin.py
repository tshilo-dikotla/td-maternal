from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalArvForm
from ..models import MaternalArv
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalArv, site=td_maternal_admin)
class MaternalArvAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = MaternalArvForm

    fieldsets = (
        (None, {
            'fields': [
                'arv_code',
                'start_date',
                'stop_date',
                'reason_for_stop',
                'reason_for_stop_other']}
         ), audit_fieldset_tuple)

    radio_fields = {'arv_code': admin.VERTICAL,
                    'reason_for_stop': admin.VERTICAL
                    }
