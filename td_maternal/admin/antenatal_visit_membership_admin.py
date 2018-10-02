from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import AntenatalVisitMembershipForm
from ..models import AntenatalVisitMembership


@admin.register(AntenatalVisitMembership, site=td_maternal_admin)
class AntenataVisitMembershipAdmin(admin.ModelAdmin):

    form = AntenatalVisitMembershipForm

    search_fields = ['registered_subject__subject_identifier',
                     'registered_subject__initials']

    radio_fields = {'antenatal_visits': admin.VERTICAL}

    list_display = (
        'registered_subject', 'report_datetime', 'antenatal_visits')


admin.site.register(AntenatalVisitMembership, AntenataVisitMembershipAdmin)
