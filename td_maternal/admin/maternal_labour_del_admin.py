from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalLabourDelForm, MaternalHivInterimHxForm
from ..models import MaternalLabourDel, MaternalHivInterimHx


@admin.register(MaternalLabourDel, site=td_maternal_admin)
class MaternalLabourDelAdmin(admin.ModelAdmin):

    dashboard_type = 'maternal'
    form = MaternalLabourDelForm

    list_display = ('registered_subject',
                    'delivery_datetime',
                    'labour_hrs',
                    'delivery_hospital',
                    'valid_regiment_duration')

    list_filter = ('delivery_hospital',
                   'valid_regiment_duration')

    search_fields = ('registered_subject__subject_identifier', )

    radio_fields = {'delivery_time_estimated': admin.VERTICAL,
                    'delivery_hospital': admin.VERTICAL,
                    'valid_regiment_duration': admin.VERTICAL,
                    'mode_delivery': admin.VERTICAL,
                    'csection_reason': admin.VERTICAL,
                    'csection_reason': admin.VERTICAL, }
    filter_horizontal = ('delivery_complications',)


@admin.register(MaternalHivInterimHx, site=td_maternal_admin)
class MaternalHivInterimHxAdmin(admin.ModelAdmin):

    form = MaternalHivInterimHxForm

    radio_fields = {'has_cd4': admin.VERTICAL,
                    'has_vl': admin.VERTICAL,
                    'vl_detectable': admin.VERTICAL}
