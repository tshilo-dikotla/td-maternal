from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..models import MaternalRando
from ..forms import MaternalRandomizationForm


@admin.register(MaternalRando, site=td_maternal_admin)
class MartenalRandoAdmin(admin.ModelAdmin):

    form = MaternalRandomizationForm

    fields = (
        'maternal_visit', 'dispensed',
        'comment', 'subject_identifier',
        'initials', 'site', 'randomization_datetime',
        'delivery_clinic')

    list_filter = ('randomization_datetime', 'site')
    readonly_fields = (
        'sid',
        'subject_identifier',
        'initials',
        'rx',
        'site',
        'randomization_datetime')
    radio_fields = {"delivery_clinic": admin.VERTICAL, }
