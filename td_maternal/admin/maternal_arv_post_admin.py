from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from ..admin_site import td_maternal_admin
from ..forms import MaternalArvPostForm, MaternalArvPostMedForm, MaternalArvPostAdhForm
from ..models import MaternalArvPost, MaternalArvPostMed, MaternalArvPostAdh


class MaternalArvPostModInlineAdmin(TabularInlineMixin):

    model = MaternalArvPostMed
    form = MaternalArvPostMedForm
    extra = 1


@admin.register(MaternalArvPostMed, site=td_maternal_admin)
class MaternalArvPostModAdmin(admin.ModelAdmin):

    form = MaternalArvPostMedForm
    list_display = ('maternal_arv_post', 'arv_code',
                    'dose_status', 'modification_date', 'modification_code')

    radio_fields = {
        "arv_code": admin.VERTICAL,
        "dose_status": admin.VERTICAL,
        "modification_code": admin.VERTICAL,
    }


@admin.register(MaternalArvPost, site=td_maternal_admin)
class MaternalArvPostAdmin(admin.ModelAdmin):

    form = MaternalArvPostForm

    fields = (
        "maternal_visit",
        "on_arv_since",
        "on_arv_reason",
        "on_arv_reason_other",
        "arv_status")

    radio_fields = {
        "on_arv_since": admin.VERTICAL,
        "on_arv_reason": admin.VERTICAL,
        "arv_status": admin.VERTICAL}
    inlines = [MaternalArvPostModInlineAdmin, ]


@admin.register(MaternalArvPostAdh, site=td_maternal_admin)
class MaternalArvPostAdhAdmin(admin.ModelAdmin):

    form = MaternalArvPostAdhForm
    fields = (
        "maternal_visit",
        "missed_doses",
        "missed_days",
        "missed_days_discnt",
        "comment")
