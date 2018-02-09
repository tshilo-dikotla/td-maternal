from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalPostPartumDepForm
from ..models import MaternalPostPartumDep


@admin.register(MaternalPostPartumDep, site=td_maternal_admin)
class MaternalPostPartumDepAdmin(admin.ModelAdmin):

    form = MaternalPostPartumDepForm
    list_display = ('maternal_visit', 'laugh', 'enjoyment', 'blame')
    radio_fields = {'laugh': admin.VERTICAL,
                    'enjoyment': admin.VERTICAL,
                    'blame': admin.VERTICAL,
                    'anxious': admin.VERTICAL,
                    'panick': admin.VERTICAL,
                    'top': admin.VERTICAL,
                    'unhappy': admin.VERTICAL,
                    'sad': admin.VERTICAL,
                    'crying': admin.VERTICAL,
                    'self_harm': admin.VERTICAL}
