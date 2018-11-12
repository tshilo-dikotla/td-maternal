from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_protocol.validators import date_not_before_study_start
from edc_base.model_validators import date_not_future
from td_maternal.models.subject_screening import MaternalEligibility


CONSENT_VERSION = (
    ('1', 'Consent version 1'),
    ('3', 'Consent version 3'))


class TdConsentVersion(BaseUuidModel):

    maternal_eligibility = models.ForeignKey(
        MaternalEligibility, on_delete=PROTECT, null=True)

    version = models.CharField(
        verbose_name="Which version of the consent would you like to "
        "be consented with.",
        choices=CONSENT_VERSION,
        max_length=3)

    report_datetime = models.DateField(
        verbose_name="Report datetime.",
        validators=[
            date_not_before_study_start,
            date_not_future, ],
        null=True,
        blank=True)

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'TD Consent Version'
        verbose_name_plural = 'TD Consent Version'
