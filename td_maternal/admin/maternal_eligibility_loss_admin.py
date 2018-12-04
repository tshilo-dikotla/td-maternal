from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..forms import MaternalEligibilityLossForm
from ..admin_site import td_maternal_admin
from ..models import MaternalEligibilityLoss
from td_maternal.admin.modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalEligibilityLoss, site=td_maternal_admin)
class MaternalEligibilityLossAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = MaternalEligibilityLossForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_screening',
                'report_datetime',
                'reason_ineligible']}
         ), audit_fieldset_tuple)

    list_display = (
        'reason_ineligible', 'report_datetime',)
