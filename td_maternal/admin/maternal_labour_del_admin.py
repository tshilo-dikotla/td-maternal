from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalLabourDelForm, MaternalHivInterimHxForm
from ..models import MaternalLabourDel, MaternalHivInterimHx
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalLabourDel, site=td_maternal_admin)
class MaternalLabourDelAdmin(ModelAdminMixin, admin.ModelAdmin):

    dashboard_type = 'maternal'
    form = MaternalLabourDelForm

    list_display = ('delivery_datetime',
                    'labour_hrs',
                    'delivery_hospital',
                    'valid_regiment_duration')

    list_filter = ('delivery_hospital',
                   'valid_regiment_duration')

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'delivery_datetime',
                'delivery_time_estimated',
                'delivery_hospital',
                'delivery_hospital_other',
                'labour_hrs',
                'mode_delivery',
                'mode_delivery_other',
                'csection_reason',
                'csection_reason_other',
                'delivery_complications',
                'delivery_complications_other',
                'live_infants_to_register',
                'still_births',
                'valid_regiment_duration',
                'arv_initiation_date',
                'delivery_comment',
                'comment']}
         ), audit_fieldset_tuple)

    search_fields = ('subject_identifier', )

    radio_fields = {'delivery_time_estimated': admin.VERTICAL,
                    'delivery_hospital': admin.VERTICAL,
                    'valid_regiment_duration': admin.VERTICAL,
                    'mode_delivery': admin.VERTICAL,
                    'csection_reason': admin.VERTICAL,
                    'csection_reason': admin.VERTICAL, }
    filter_horizontal = ('delivery_complications',)


@admin.register(MaternalHivInterimHx, site=td_maternal_admin)
class MaternalHivInterimHxAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalHivInterimHxForm
    fieldsets = (
        (None, {
            'fields': [
                'has_cd4',
                'cd4_date',
                'cd4_result',
                'has_vl',
                'vl_date',
                'vl_detectable',
                'vl_result',
                'comment']}
         ), audit_fieldset_tuple)

    radio_fields = {'has_cd4': admin.VERTICAL,
                    'has_vl': admin.VERTICAL,
                    'vl_detectable': admin.VERTICAL}
