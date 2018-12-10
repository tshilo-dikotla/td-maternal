from django.db import models
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import TrackingIdentifierModelMixin
from edc_protocol.validators import date_not_before_study_start
from edc_visit_schedule.model_mixins import OffScheduleModelMixin

from ..choices import OFF_STUDY_REASON


class MaternalOffStudy(OffScheduleModelMixin,
                       TrackingIdentifierModelMixin, BaseUuidModel):

    tracking_identifier_prefix = 'ST'

    offstudy_date = models.DateField(
        verbose_name="Off-study Date",
        validators=[
            date_not_before_study_start,
            date_not_future])

    reason = models.CharField(
        verbose_name="Please code the primary reason participant taken off-study",
        max_length=115,
        choices=OFF_STUDY_REASON)

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
