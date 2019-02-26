from django.db import models
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import TrackingIdentifierModelMixin
from edc_protocol.validators import date_not_before_study_start
from edc_protocol.validators import datetime_not_before_study_start
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_schedule.model_mixins import OffScheduleModelMixin

from ..choices import OFF_STUDY_REASON


class MaternalOffStudy(OffScheduleModelMixin, ReferenceModelMixin,
                       TrackingIdentifierModelMixin, BaseUuidModel):

    tracking_identifier_prefix = 'ST'

    offstudy_date = models.DateField(
        verbose_name="Off-study Date",
        null=True,
        default=get_utcnow,
        validators=[
            date_not_before_study_start,
            date_not_future])

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        null=True,
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    reason = models.CharField(
        verbose_name="Please code the primary reason participant taken off-study",
        max_length=115,
        choices=OFF_STUDY_REASON,
        null=True)

    reason_other = OtherCharField()

    comment = models.TextField(
        max_length=250,
        verbose_name="Comment",
        blank=True,
        null=True)

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.last_study_fu_date:
            self.last_study_fu_date = self.offschedule_datetime.date()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Maternal Off Study'
        verbose_name_plural = 'Maternal Off Studies'
