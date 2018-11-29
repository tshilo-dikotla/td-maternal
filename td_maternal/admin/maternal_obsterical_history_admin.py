from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalObstericalHistoryForm
from ..models import MaternalObstericalHistory
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalObstericalHistory, site=td_maternal_admin)
class MaternalObstericalHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalObstericalHistoryForm
    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'prev_pregnancies',
                'pregs_24wks_or_more',
                'lost_before_24wks',
                'lost_after_24wks',
                'live_children',
                'children_died_b4_5yrs',
                'children_deliv_before_37wks',
                'children_deliv_aftr_37wks']}
         ), audit_fieldset_tuple)

    list_display = ('maternal_visit',
                    'prev_pregnancies',
                    'pregs_24wks_or_more',
                    'lost_before_24wks',
                    'lost_after_24wks',
                    'live_children')
