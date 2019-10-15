from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, audit_fields

from edc_consent.actions import (
    flag_as_verified_against_paper, unflag_as_verified_against_paper)

from ..admin_site import td_maternal_admin
from ..forms import KaraboSubjectConsentForm
from ..models import KaraboSubjectConsent
from .modeladmin_mixins import ModelAdminMixin


@admin.register(KaraboSubjectConsent, site=td_maternal_admin)
class KaraboSubjectConsentAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = KaraboSubjectConsentForm

    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'subject_identifier',
                'screening_identifier',
                'first_name',
                'last_name',
                'initials',
                'dob',
                'is_dob_estimated',
                'language',
                'is_literate',
                'guardian_name',
                'consent_datetime',
                'identity',
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'consent_signature',
                'consent_copy'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'is_literate': admin.VERTICAL,
        'language': admin.VERTICAL,
        'consent_reviewed': admin.VERTICAL,
        'study_questions': admin.VERTICAL,
        'assessment_score': admin.VERTICAL,
        'consent_signature': admin.VERTICAL,
        'consent_copy': admin.VERTICAL,
        'is_dob_estimated': admin.VERTICAL
    }

    list_display = ('subject_identifier',
                    'verified_by',
                    'is_verified',
                    'is_verified_datetime',
                    'first_name',
                    'last_name',
                    'initials',
                    'identity',)

    search_fields = ('subject_identifier',)

    actions = [
        flag_as_verified_against_paper,
        unflag_as_verified_against_paper, ]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'td_maternal.change_karabosubjectconsent' not in request.user.get_group_permissions():
            del actions['flag_as_verified_against_paper']
            del actions['unflag_as_verified_against_paper']
        return actions

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)
