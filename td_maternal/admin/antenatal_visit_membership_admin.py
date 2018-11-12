from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import AntenatalVisitMembershipForm
from ..models import AntenatalVisitMembership
from td_maternal.admin.modeladmin_mixins import ModelAdminMixin


@admin.register(AntenatalVisitMembership, site=td_maternal_admin)
class AntenataVisitMembershipAdmin(admin.ModelAdmin, ModelAdminMixin):

    form = AntenatalVisitMembershipForm

    search_fields = ['subject_identifier']

    radio_fields = {'antenatal_visits': admin.VERTICAL}

    list_display = (
        'report_datetime', 'antenatal_visits')


admin.site.register(AntenatalVisitMembership, AntenataVisitMembershipAdmin)
