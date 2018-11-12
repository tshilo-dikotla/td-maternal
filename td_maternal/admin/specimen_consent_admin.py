from django.contrib import admin
from ..admin_site import td_maternal_admin
from edc_consent.actions import (
    flag_as_verified_against_paper, unflag_as_verified_against_paper)

from ..forms import SpecimenConsentForm
from ..models import SpecimenConsent
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SpecimenConsent, site=td_maternal_admin)
class SpecimenConsentAdmin(admin.ModelAdmin, ModelAdminMixin):

    form = SpecimenConsentForm

    fields = ('registered_subject',
              'consent_datetime',
              'language',
              'may_store_samples',
              'is_literate',
              'witness_name',
              'purpose_explained',
              'purpose_understood',
              )
    radio_fields = {'language': admin.VERTICAL,
                    'may_store_samples': admin.VERTICAL,
                    'is_literate': admin.VERTICAL, }

    list_display = ('subject_identifier',
                    'registered_subject',
                    'created',
                    'modified',
                    'user_created',
                    'user_modified')
    list_filter = ('language',
                   'is_literate')
    actions = [
        flag_as_verified_against_paper,
        unflag_as_verified_against_paper, ]
