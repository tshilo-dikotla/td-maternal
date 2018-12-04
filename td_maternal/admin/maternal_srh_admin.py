from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalSrhForm
from ..models import MaternalSrh
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalSrh, site=td_maternal_admin)
class MaternalSrhAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = MaternalSrhForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'seen_at_clinic',
                'reason_unseen_clinic',
                'reason_unseen_clinic_other',
                'is_contraceptive_initiated',
                'contr',
                'contr_other',
                'reason_not_initiated',
                'reason_not_initiated_other']}
         ), audit_fieldset_tuple)

    radio_fields = {'seen_at_clinic': admin.VERTICAL,
                    'reason_unseen_clinic': admin.VERTICAL,
                    'is_contraceptive_initiated': admin.VERTICAL,
                    'reason_not_initiated': admin.VERTICAL
                    }

    filter_horizontal = ('contr', )
