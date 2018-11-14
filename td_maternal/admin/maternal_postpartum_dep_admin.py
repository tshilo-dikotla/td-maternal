from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalPostPartumDepForm
from ..models import MaternalPostPartumDep
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin import audit_fieldset_tuple


@admin.register(MaternalPostPartumDep, site=td_maternal_admin)
class MaternalPostPartumDepAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalPostPartumDepForm
    list_display = ('maternal_visit', 'laugh', 'enjoyment', 'blame')

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'laugh',
                'enjoyment',
                'blame',
                'anxious',
                'panick',
                'top',
                'unhappy',
                'sad',
                'crying',
                'self_harm']}
         ), audit_fieldset_tuple)

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
