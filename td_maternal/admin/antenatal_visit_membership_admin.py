from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import AntenatalVisitMembershipForm
from ..models import AntenatalVisitMembership
from td_maternal.admin.modeladmin_mixins import ModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(AntenatalVisitMembership, site=td_maternal_admin)
class AntenataVisitMembershipAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AntenatalVisitMembershipForm

    search_fields = ['subject_identifier']

    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'antenatal_visits']}
         ), audit_fieldset_tuple)

    radio_fields = {'antenatal_visits': admin.VERTICAL}

    list_display = (
        'report_datetime', 'antenatal_visits')


admin.site.register(AntenatalVisitMembership, AntenataVisitMembershipAdmin)
