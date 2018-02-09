from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalPostPartumFuForm
from ..models import MaternalPostPartumFu


@admin.register(MaternalPostPartumFu, site=td_maternal_admin)
class MaternalPostPartumFuAdmin(admin.ModelAdmin):

    form = MaternalPostPartumFuForm
    fields = ('maternal_visit',
              'report_datetime',
              'new_diagnoses',
              'diagnoses',
              'diagnoses_other',
              'hospitalized',
              'hospitalization_reason',
              'hospitalization_reason_other',
              'hospitalization_days',
              'has_who_dx',
              'who')
    list_display = ('maternal_visit', 'new_diagnoses', 'has_who_dx')
    list_filter = ('new_diagnoses', 'diagnoses', 'has_who_dx')
    radio_fields = {'new_diagnoses': admin.VERTICAL,
                    'hospitalized': admin.VERTICAL,
                    'has_who_dx': admin.VERTICAL}
    filter_horizontal = ('who', 'diagnoses', 'hospitalization_reason')
