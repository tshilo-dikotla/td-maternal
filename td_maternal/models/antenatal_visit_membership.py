from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import datetime_not_future
from edc_protocol.validators import datetime_not_before_study_start
from edc_constants.choices import YES_NO
from edc_registration.models import RegisteredSubject


from .maternal_consent import SubjectConsent


class AntenatalVisitMembership(BaseUuidModel):

    consent_model = SubjectConsent

    registered_subject = models.OneToOneField(
        RegisteredSubject, on_delete=PROTECT, null=True)

    report_datetime = models.DateTimeField(
        verbose_name="Report date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        help_text='')

    antenatal_visits = models.CharField(
        verbose_name='Are you ready to start the antenatal enrollment visits?',
        choices=YES_NO,
        help_text='',
        max_length=3)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        super(AntenatalVisitMembership, self).save(*args, **kwargs)

    def __str__(self):
        return "{0}".format(self.registered_subject.subject_identifier)

    def natural_key(self):
        return self.registered_subject.natural_key()
    natural_key.dependencies = ['edc_registration.registeredsubject']

    def get_registration_datetime(self):
        return self.report_datetime

    @property
    def subject_identifier(self):
        return self.registered_subject.subject_identifier

    def get_subject_identifier(self):
        return self.registered_subject.subject_identifier

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Antenatal Visit Membership'
        verbose_name_plural = 'Antenatal Visit Membership'
