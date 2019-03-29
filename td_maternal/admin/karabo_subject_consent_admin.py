from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_maternal_admin
from ..forms import KaraboSubjectConsentForm
from ..models import KaraboSubjectConsent


@admin.register(KaraboSubjectConsent, site=td_maternal_admin)
class KaraboSubjectConsentAdmin(admin.ModelAdmin):
    form = KaraboSubjectConsentForm

    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'name',
                'surname',
                'initials',
                'consent_lang',
                'literacy',
                'witness_name',
                'consent_datetime',
                'omang',
                'review',
                'answer',
                'questions',
                'signed_consent',
                'offer'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'literacy': admin.VERTICAL,
        'review': admin.VERTICAL,
        'answer': admin.VERTICAL,
        'questions': admin.VERTICAL,
        'signed_consent': admin.VERTICAL,
        'offer': admin.VERTICAL
    }
