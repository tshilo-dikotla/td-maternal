from django.apps import apps
from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_protocol.validators import datetime_not_before_study_start
from edc_base.model_validators import datetime_not_future
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO
from edc_registration.models import RegisteredSubject
from uuid import uuid4

from .eligibility import Eligibility


class MaternalEligibility(BaseUuidModel):
    """ A model completed by the user to test and capture the result of
    the pre-consent eligibility checks.

    This model has no PII.
    """

    registered_subject = models.OneToOneField(
        RegisteredSubject, on_delete=PROTECT, null=True)

    eligibility_id = models.CharField(
        verbose_name="Eligibility Identifier",
        max_length=36,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        help_text='Date and time of assessing eligibility')

    age_in_years = models.IntegerField(
        verbose_name='What is the age of the participant?')

    has_omang = models.CharField(
        verbose_name="Do you have an OMANG?",
        max_length=3,
        choices=YES_NO)

    ineligibility = models.TextField(
        verbose_name="Reason not eligible",
        max_length=150,
        null=True,
        editable=False)

    is_eligible = models.BooleanField(
        default=False,
        editable=False)
    # is updated via signal once subject is consented
    is_consented = models.BooleanField(
        default=False,
        editable=False)
    # updated by signal on saving consent, is determined by participant
    # citizenship
    has_passed_consent = models.BooleanField(
        default=False,
        editable=False)

    history = HistoricalRecords()

    class Meta:
        app_label = 'td_maternal'
        verbose_name = "Maternal Eligibility"
        verbose_name_plural = "Maternal Eligibility"

    def save(self, *args, **kwargs):
        eligibility_criteria = Eligibility(self.age_in_years, self.has_omang)
        self.set_uuid_for_eligibility_if_none()
        self.is_eligible = eligibility_criteria.is_eligible
        self.ineligibility = eligibility_criteria.error_message
        super(MaternalEligibility, self).save(*args, **kwargs)

    def natural_key(self):
        return self.eligibility_id

    @property
    def maternal_eligibility_loss(self):
        MaternalEligibilityLoss = apps.get_model(
            'td_maternal', 'MaternalEligibilityLoss')
        try:
            maternal_eligibility_loss = MaternalEligibilityLoss.objects.get(
                maternal_eligibility_id=self.id)
        except MaternalEligibilityLoss.DoesNotExist:
            maternal_eligibility_loss = None
        return maternal_eligibility_loss

    def set_uuid_for_eligibility_if_none(self):
        if not self.eligibility_id:
            self.eligibility_id = str(uuid4())
