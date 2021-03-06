from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import (MaternalArvPostForm,
                     MaternalArvPostMedForm, MaternalArvPostAdhForm)
from ..models import MaternalArvPost, MaternalArvPostMed, MaternalArvPostAdh
from .modeladmin_mixins import CrfModelAdminMixin, ModelAdminMixin


class MaternalArvPostMedInlineAdmin(TabularInlineMixin, admin.TabularInline):

    model = MaternalArvPostMed
    form = MaternalArvPostMedForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': [
                'arv_code',
                'dose_status',
                'modification_date',
                'modification_code']}
         ), audit_fieldset_tuple)


@admin.register(MaternalArvPostMed, site=td_maternal_admin)
class MaternalArvPostMedAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalArvPostMedForm
    list_display = ('maternal_arv_post', 'arv_code',
                    'dose_status', 'modification_date', 'modification_code')
    fieldsets = (
        (None, {
            'fields': [
                'arv_code',
                'dose_status',
                'modification_date',
                'modification_code']}
         ), audit_fieldset_tuple)

    radio_fields = {
        "arv_code": admin.VERTICAL,
        "dose_status": admin.VERTICAL,
        "modification_code": admin.VERTICAL,
    }


@admin.register(MaternalArvPost, site=td_maternal_admin)
class MaternalArvPostAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalArvPostForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'on_arv_since',
                'on_arv_reason',
                'on_arv_reason_other',
                'arv_status']}
         ),)

    radio_fields = {
        "on_arv_since": admin.VERTICAL,
        "on_arv_reason": admin.VERTICAL,
        "arv_status": admin.VERTICAL}

    inlines = [MaternalArvPostMedInlineAdmin, ]


@admin.register(MaternalArvPostAdh, site=td_maternal_admin)
class MaternalArvPostAdhAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MaternalArvPostAdhForm
    fieldsets = (
        (None, {
            'fields': [
                'maternal_visit',
                'report_datetime',
                'missed_doses',
                'missed_days',
                'missed_days_discnt',
                'comment']}
         ), audit_fieldset_tuple)
