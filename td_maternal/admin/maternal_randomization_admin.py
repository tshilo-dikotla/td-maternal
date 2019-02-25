from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import MaternalRandomizationForm
from ..models import MaternalRando
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalRando, site=td_maternal_admin)
class MartenalRandoAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalRandomizationForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'dispensed',
                'comment',
                'subject_identifier',
                'initials',
                'site',
                'randomization_datetime',
                'delivery_clinic',
                'delivery_clinic_other']}
         ), audit_fieldset_tuple)

    list_filter = ('randomization_datetime', 'site')

    readonly_fields = (
        'sid',
        'subject_identifier',
        'initials',
        'rx',
        'site',
        'randomization_datetime')

    radio_fields = {'delivery_clinic': admin.VERTICAL,
                    'dispensed': admin.VERTICAL}
