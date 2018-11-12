from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_protocol.validators import datetime_not_before_study_start


from .maternal_consent import SubjectConsent


class AntenatalVisitMembership(UniqueSubjectIdentifierFieldMixin, BaseUuidModel):

    consent_model = SubjectConsent


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
        return f"{self.subject_identifier}"

#     def natural_key(self):
#         return self.registered_subject.natural_key()
#     natural_key.dependencies = ['edc_registration.registeredsubject']

    def get_registration_datetime(self):
        return self.report_datetime


    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Antenatal Visit Membership'
        verbose_name_plural = 'Antenatal Visit Membership'
