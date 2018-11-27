from django.db import models

from edc_metadata.managers import CrfMetadataManager
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_export.model_mixins import ExportTrackingFieldsModelMixin
from edc_offstudy.models import OffStudyMixin
from edc_visit_tracking.model_mixins import CrfModelMixin

# from ..managers import VisitCrfModelManager

from .subject_consent import SubjectConsent
from .maternal_visit import MaternalVisit


class MaternalCrfModel(CrfModelMixin, ExportTrackingFieldsModelMixin,
                       OffStudyMixin, RequiresConsentFieldsModelMixin, BaseUuidModel):

    """ Base model for all scheduled models
    s(adds key to :class:`MaternalVisit`). """

    consent_model = SubjectConsent

    visit_model_attr = 'maternal_visit'

    off_study_model = ('td_maternal', 'MaternalOffStudy')

    maternal_visit = models.OneToOneField(
        MaternalVisit, on_delete=models.CASCADE)

#     objects = VisitCrfModelManager()

    entry_meta_data_manager = CrfMetadataManager()

    def __str__(self):
        return "{}: {}".format(self.__class__._meta.model_name,
                               self.maternal_visit.appointment.registered_subject.subject_identifier)

    def natural_key(self):
        return self.maternal_visit.natural_key()

    class Meta:
        abstract = True
