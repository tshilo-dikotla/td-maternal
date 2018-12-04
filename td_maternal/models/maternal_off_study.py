from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import TrackingIdentifierModelMixin
from edc_visit_schedule.model_mixins import OffScheduleModelMixin


class MaternalOffStudy(OffScheduleModelMixin,
                       TrackingIdentifierModelMixin, BaseUuidModel):

    tracking_identifier_prefix = 'ST'

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.last_study_fu_date:
            self.last_study_fu_date = self.offschedule_datetime.date()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Maternal Off Study'
        verbose_name_plural = 'Maternal Off Studies'
