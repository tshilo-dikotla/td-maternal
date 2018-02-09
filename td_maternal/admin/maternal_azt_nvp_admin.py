from django.contrib import admin

from ..admin_site import td_maternal_admin
from ..forms import MaternalAztNvpForm
from ..models import MaternalAztNvp


@admin.register(MaternalAztNvp, site=td_maternal_admin)
class MaternalAztNvpAdmin(admin.ModelAdmin):

    form = MaternalAztNvpForm

    radio_fields = {'azt_nvp_delivery': admin.VERTICAL,
                    'instructions_given': admin.VERTICAL}

    list_display = (
        'report_datetime', 'date_given', 'azt_nvp_delivery', 'instructions_given')

    list_filter = (
        'report_datetime', 'date_given', 'azt_nvp_delivery', 'instructions_given')
