from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager
from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins import OnScheduleModelMixin

from .model_mixins import ConsentVersionModelModelMixin


class OnScheduleAntenatalEnrollment(ConsentVersionModelModelMixin,
                                    OnScheduleModelMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by subject_consent.
    """
    schedule_name = models.CharField(max_length=25,
                                     blank=True,
                                     null=True)

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def put_on_schedule(self):
        pass

    class Meta:
        pass


class OnScheduleAntenatalVisitMembership(ConsentVersionModelModelMixin,
                                         OnScheduleModelMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by subject_consent.
    """
    schedule_name = models.CharField(max_length=25,
                                     blank=True,
                                     null=True)

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def put_on_schedule(self):
        pass

    class Meta:
        pass


class OnScheduleMaternalLabourDel(ConsentVersionModelModelMixin,
                                  OnScheduleModelMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by subject_consent.
    """
    schedule_name = models.CharField(max_length=25,
                                     blank=True,
                                     null=True)

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def put_on_schedule(self):
        pass

    class Meta:
        pass
