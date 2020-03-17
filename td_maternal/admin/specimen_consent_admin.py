from collections import OrderedDict
from django.contrib import admin
from edc_consent.actions import (
    flag_as_verified_against_paper, unflag_as_verified_against_paper)
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import SpecimenConsentForm
from ..models import SpecimenConsent
from .exportaction_mixin import ExportActionMixin
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SpecimenConsent, site=td_maternal_admin)
class SpecimenConsentAdmin(ModelAdminMixin, ExportActionMixin, admin.ModelAdmin):

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
                    'verified_by',
                    'is_verified',
                    'is_verified_datetime',
                    'created',
                    'modified',
                    'user_created',
                    'user_modified')
    list_filter = ('language',
                   'is_literate',
                   'is_verified',
                   'verified_by',)

    search_fields = ('subject_identifier',)

    def get_actions(self, request):

        super_actions = super().get_actions(request)

        if ('td_maternal.change_subjectconsent'
                in request.user.get_group_permissions()):

            consent_actions = [
                flag_as_verified_against_paper,
                unflag_as_verified_against_paper]

            # Add actions from this ModelAdmin.
            actions = (self.get_action(action) for action in consent_actions)
            # get_action might have returned None, so filter any of those out.
            actions = filter(None, actions)

            actions = self._filter_actions_by_permissions(request, actions)
            # Convert the actions into an OrderedDict keyed by name.
            actions = OrderedDict(
                (name, (func, name, desc))
                for func, name, desc in actions
            )

            super_actions.update(actions)

        return super_actions
