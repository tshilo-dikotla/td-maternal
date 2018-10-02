from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import AntenatalEnrollmentForm
from ..models import AntenatalEnrollment


@admin.register(AntenatalEnrollment, site=td_maternal_admin)
class AntenatalEnrollmentAdmin(admin.ModelAdmin):

    form = AntenatalEnrollmentForm

    search_fields = ['registered_subject__subject_identifier',
                     'registered_subject__initials']

    fields = ('registered_subject',
              'report_datetime',
              'knows_lmp',
              'last_period_date',
              'edd_by_lmp',
              'ga_lmp_enrollment_wks',
              'ga_lmp_anc_wks',
              'is_diabetic',
              'will_breastfeed',
              'will_remain_onstudy',
              'current_hiv_status',
              'evidence_hiv_status',
              'week32_test',
              'week32_test_date',
              'week32_result',
              'evidence_32wk_hiv_status',
              'will_get_arvs',
              'rapid_test_done',
              'rapid_test_date',
              'rapid_test_result',
              'enrollment_hiv_status')
    readonly_fields = (
        'edd_by_lmp', 'ga_lmp_enrollment_wks', 'enrollment_hiv_status')
    radio_fields = {'is_diabetic': admin.VERTICAL,
                    'will_breastfeed': admin.VERTICAL,
                    'will_remain_onstudy': admin.VERTICAL,
                    'current_hiv_status': admin.VERTICAL,
                    'week32_test': admin.VERTICAL,
                    'week32_result': admin.VERTICAL,
                    'evidence_32wk_hiv_status': admin.VERTICAL,
                    'evidence_hiv_status': admin.VERTICAL,
                    'will_get_arvs': admin.VERTICAL,
                    'rapid_test_done': admin.VERTICAL,
                    'rapid_test_result': admin.VERTICAL,
                    'knows_lmp': admin.VERTICAL}
    list_display = (
        'registered_subject', 'report_datetime', 'evidence_hiv_status',
        'will_get_arvs', 'ga_lmp_anc_wks', 'enrollment_hiv_status')
