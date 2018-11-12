from django.contrib import admin
from ..admin_site import td_maternal_admin
from ..forms import MaternalEligibilityLossForm
from ..models import MaternalEligibilityLoss
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalEligibilityLoss, site=td_maternal_admin)
class MaternalEligibilityLossAdmin(admin.ModelAdmin, ModelAdminMixin):

    form = MaternalEligibilityLossForm

    fields = ('maternal_eligibility',
              'report_datetime',
              'reason_ineligible')
