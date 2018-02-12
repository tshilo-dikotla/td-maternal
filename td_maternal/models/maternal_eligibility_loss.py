from django.db import models
from django.utils import timezone
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords

from .maternal_eligibility import MaternalEligibility


class MaternalEligibilityLoss(BaseUuidModel):
    """ A model triggered and completed by system when a mother is in-eligible. """

    maternal_eligibility = models.OneToOneField(
        MaternalEligibility, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=timezone.now,
        help_text='Date and time of report.')

    reason_ineligible = models.TextField(
        verbose_name='Reason not eligible',
        max_length=500,
        help_text='Gets reasons from Maternal Eligibility.ineligibility')

    history = HistoricalRecords()

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Maternal Eligibility Loss'
