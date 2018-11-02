from django.contrib import admin
from edc_consent.actions import (
    flag_as_verified_against_paper, unflag_as_verified_against_paper)

from ..admin_site import td_maternal_admin
from ..forms import SubjectConsentForm
from ..models import SubjectConsent, MaternalEligibility


@admin.register(SubjectConsent, site=td_maternal_admin)
class SubjectConsentAdmin(admin.ModelAdmin):

    form = SubjectConsentForm

    fields = ('maternal_eligibility',
              'first_name',
              'last_name',
              'initials',
              'language',
              #               'study_site',
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
              'comment',
              'consent_reviewed',
              'study_questions',
              'assessment_score',
              'consent_signature',
              'consent_copy')

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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_eligibility":
            kwargs["queryset"] = MaternalEligibility.objects.filter(
                registered_subject__id__exact=request.GET.get('registered_subject'))
        else:
            self.readonly_fields = list(self.readonly_fields)
            try:
                self.readonly_fields.index('registered_subject')
            except ValueError:
                self.readonly_fields.append('registered_subject')
        return super(SubjectConsentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
