from django.contrib import admin
from edc_consent.actions import (
    flag_as_verified_against_paper, unflag_as_verified_against_paper)
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import SpecimenConsentForm
from ..models import SpecimenConsent
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SpecimenConsent, site=td_maternal_admin)
class SpecimenConsentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SpecimenConsentForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'consent_datetime',
                'language',
                'may_store_samples',
                'is_literate',
                'witness_name',
                'consent_reviewed',
                'assessment_score',
                'consent_copy']}
         ), audit_fieldset_tuple)

    radio_fields = {'language': admin.VERTICAL,
                    'may_store_samples': admin.VERTICAL,
                    'is_literate': admin.VERTICAL,
                    'consent_reviewed': admin.VERTICAL,
                    'assessment_score': admin.VERTICAL,
                    'consent_copy': admin.VERTICAL, }

    list_display = ('subject_identifier',
                    'created',
                    'modified',
                    'user_created',
                    'user_modified')
    list_filter = ('language',
                   'is_literate')
    actions = [
        flag_as_verified_against_paper,
        unflag_as_verified_against_paper, ]
