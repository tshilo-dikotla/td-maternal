from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from ..admin_site import td_maternal_admin
from ..forms import MaternalArvPregForm, MaternalArvForm
from ..models import MaternalArvPreg, MaternalArv
from .modeladmin_mixins import CrfModelAdminMixin, ModelAdminMixin


class MaternalArvInlineAdmin(TabularInlineMixin, admin.TabularInline):
    model = MaternalArv
    form = MaternalArvForm
    extra = 1
    min_num = 3


@admin.register(MaternalArv, site=td_maternal_admin)
class MaternalArvAdmin(admin.ModelAdmin, ModelAdminMixin):
    form = MaternalArvForm


@admin.register(MaternalArvPreg, site=td_maternal_admin)
class MaternalArvPregAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = MaternalArvPregForm
    inlines = [MaternalArvInlineAdmin, ]
    list_display = ('maternal_visit', 'took_arv',)
    list_filter = ('took_arv',)

    radio_fields = {'took_arv': admin.VERTICAL,
                    'is_interrupt': admin.VERTICAL,
                    'interrupt': admin.VERTICAL
                    }
