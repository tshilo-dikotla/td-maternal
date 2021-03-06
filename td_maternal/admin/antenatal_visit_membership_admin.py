from td_maternal.admin.modeladmin_mixins import ModelAdminMixin

from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import AntenatalVisitMembershipForm
from ..models import AntenatalVisitMembership


@admin.register(AntenatalVisitMembership, site=td_maternal_admin)
class AntenataVisitMembershipAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AntenatalVisitMembershipForm

    search_fields = ['subject_identifier']

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'antenatal_visits']}
         ), audit_fieldset_tuple)

    radio_fields = {'antenatal_visits': admin.VERTICAL}

    list_display = (
        'subject_identifier', 'report_datetime', 'antenatal_visits')


admin.site.register(AntenatalVisitMembership, AntenataVisitMembershipAdmin)
