from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalMedicalHistoryForm
from ..models import MaternalMedicalHistory


@admin.register(MaternalMedicalHistory, site=td_maternal_admin)
class MaternalMedicalHistoryAdmin(admin.ModelAdmin):

    form = MaternalMedicalHistoryForm

    list_display = ('maternal_visit', 'chronic_since', 'sero_posetive', 'date_hiv_diagnosis', 'perinataly_infected',
                    'lowest_cd4_known', 'cd4_count', 'cd4_date')
    list_filter = (
        'chronic_since', 'sero_posetive', 'date_hiv_diagnosis', 'perinataly_infected')
    radio_fields = {'chronic_since': admin.VERTICAL,
                    'who_diagnosis': admin.VERTICAL,
                    'sero_posetive': admin.VERTICAL,
                    'perinataly_infected': admin.VERTICAL,
                    'know_hiv_status': admin.VERTICAL,
                    'lowest_cd4_known': admin.VERTICAL,
                    'is_date_estimated': admin.VERTICAL}
    filter_horizontal = (
        'who', 'mother_chronic', 'father_chronic', 'mother_medications')
