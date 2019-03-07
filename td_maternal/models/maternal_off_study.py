from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import date_not_before_study_start
from edc_protocol.validators import datetime_not_before_study_start
from edc_visit_schedule.model_mixins import OffScheduleModelMixin
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from ..action_items import MATERNALOFF_STUDY_ACTION
from ..choices import OFF_STUDY_REASON
from .onschedule import OnScheduleAntenatalEnrollment
from .onschedule import OnScheduleAntenatalVisitMembership, OnScheduleMaternalLabourDel


class MaternalOffStudy(OffScheduleModelMixin, ActionModelMixin, BaseUuidModel):

    tracking_identifier_prefix = 'ST'

    action_name = MATERNALOFF_STUDY_ACTION

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

    def take_off_schedule(self):
        v1_schedules = [OnScheduleMaternalLabourDel, OnScheduleAntenatalVisitMembership,
                        OnScheduleAntenatalEnrollment]

        for on_schedule in v1_schedules:
            try:
                on_schedule.objects.get(
                    subject_identifier=self.subject_identifier)
                print('>>>>>>>>>>>>>>>>>>>>>>>>')
                _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                    on_schedule._meta.label_lower, name=on_schedule.schedule_name)
                print('<><><><><><><><><><><><><><>', schedule)
                schedule.take_off_schedule(offschedule_model_obj=self)
            except ObjectDoesNotExist:
                pass

    class Meta:
        verbose_name = 'Maternal Off Study'
        verbose_name_plural = 'Maternal Off Studies'
