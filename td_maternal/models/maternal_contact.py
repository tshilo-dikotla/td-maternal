from django.db import models
from django.db.models.deletion import PROTECT
from django.utils import timezone

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_constants.choices import YES_NO
from edc_protocol.validators import datetime_not_before_study_start
from edc_registration.models import RegisteredSubject

from ..maternal_choices import CALL_REASON, CONTACT_TYPE
from .maternal_consent import MaternalConsent


class MaternalContactManager(models.Manager):

    def get_by_natural_key(self, registered_subject):
        return self.get(
            subject_identifier=registered_subject.subject_identifier)


class MaternalContact(BaseUuidModel, models.Model):

    consent_model = MaternalConsent

    report_datetime = models.DateTimeField(
        verbose_name='Report Date',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        default=timezone.now,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    registered_subject = models.ForeignKey(
        RegisteredSubject, on_delete=PROTECT)

    contact_type = models.CharField(
        verbose_name='Type of contact',
        choices=CONTACT_TYPE,
        max_length=25,
    )

    contact_datetime = models.DateTimeField(
        verbose_name='Contact datetime',
        help_text='This date can be modified.',
        null=True,
        blank=True)

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
        return (self.registered_subject.subject_identifier, )

    class Meta:
        app_label = 'td_maternal'
        unique_together = ('registered_subject', 'contact_datetime')
