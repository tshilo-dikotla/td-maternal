from django.contrib import admin
from edc_consent.actions import (
    flag_as_verified_against_paper, unflag_as_verified_against_paper)
from edc_consent.modeladmin_mixins import ModelAdminConsentMixin
from edc_model_admin import audit_fieldset_tuple, audit_fields
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import td_maternal_admin
from ..forms import SubjectConsentForm
from ..models import SubjectConsent
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectConsent, site=td_maternal_admin)
class SubjectConsentAdmin(ModelAdminConsentMixin, ModelAdminMixin,
                          SimpleHistoryAdmin, admin.ModelAdmin):

    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'subject_identifier',
                'first_name',
                'last_name',
                'initials',
                'language',
                'study_site',
                'recruit_source',
                'recruit_source_other',
                'recruitment_clinic',
                'recruitment_clinic_other',
                'is_literate',
                'witness_name',
                'consent_datetime',
                'dob',
                'is_dob_estimated',
                'citizen',
                'identity',
                'identity_type',
                'confirm_identity',
                'comment')}),
        ('Review Questions', {
            'fields': (
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'consent_signature',
                'consent_copy'),
            'description': 'The following questions are directed to the interviewer.'}),
        audit_fieldset_tuple)

    radio_fields = {
        'assessment_score': admin.VERTICAL,
        'citizen': admin.VERTICAL,
        'consent_copy': admin.VERTICAL,
        'consent_reviewed': admin.VERTICAL,
        'consent_signature': admin.VERTICAL,
        'is_dob_estimated': admin.VERTICAL,
        'is_literate': admin.VERTICAL,
        'language': admin.VERTICAL,
        'recruit_source': admin.VERTICAL,
        'recruitment_clinic': admin.VERTICAL,
        'study_questions': admin.VERTICAL}

    list_display = ('subject_identifier',
                    'is_verified',
                    'is_verified_datetime',
                    'first_name',
                    'initials',
                    'gender',
                    'dob',
                    'consent_datetime',
                    'recruit_source',
                    'recruitment_clinic',
                    'created',
                    'modified',
                    'user_created',
                    'user_modified')
    list_filter = ('language',
                   'is_verified',
                   'is_literate',
                   'identity_type')

    actions = [
        flag_as_verified_against_paper,
        unflag_as_verified_against_paper, ]

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)
