from td_maternal.models.subject_consent import SubjectConsent

from django.db import models
from django.utils import timezone
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_protocol.validators import datetime_not_before_study_start

from ..maternal_choices import CALL_REASON, CONTACT_TYPE


class MaternalContactManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(
            subject_identifier=subject_identifier)


class MaternalContact(NonUniqueSubjectIdentifierFieldMixin, BaseUuidModel):

    consent_model = SubjectConsent

    report_datetime = models.DateTimeField(
        verbose_name='Report Date',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        default=timezone.now,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    contact_type = models.CharField(
        verbose_name='Type of contact',
        choices=CONTACT_TYPE,
        max_length=25,
    )

    contact_datetime = models.DateTimeField(
        verbose_name='Contact datetime',
        help_text='This date can be modified.')

    call_reason = models.CharField(
        verbose_name='Reason for call',
        max_length=30,
        choices=CALL_REASON,
    )

    call_reason_other = models.CharField(
        verbose_name='Other, specify',
        max_length=70,
        null=True,
        blank=True
    )

    contact_success = models.CharField(
        verbose_name='Were you able to reach the participant?',
        max_length=5,
        choices=YES_NO,
        help_text='If Yes, please answer the next question.'
    )

    contact_comment = models.TextField(
        verbose_name='Outcome of call',
        max_length=500,
        null=True,
        blank=True
    )

    history = HistoricalRecords()

    objects = MaternalContactManager()

    def natural_key(self):
        return (self.subject_identifier,)

    class Meta:
        app_label = 'td_maternal'
        unique_together = ('subject_identifier', 'contact_datetime')
