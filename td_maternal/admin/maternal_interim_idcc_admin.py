from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalInterimIdccForm
from ..models import MaternalInterimIdcc


@admin.register(MaternalInterimIdcc, site=td_maternal_admin)
class MaternalInterimIdccAdmin(admin.ModelAdmin):

    form = MaternalInterimIdccForm

    radio_fields = {'info_since_lastvisit': admin.VERTICAL,
                    'value_vl_size': admin.VERTICAL}

    list_display = ('report_datetime', 'recent_cd4', 'value_vl',)

    list_filter = (
        'info_since_lastvisit', 'recent_cd4_date', 'value_vl_size', 'recent_vl_date')
