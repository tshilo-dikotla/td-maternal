from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin

from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_mixins import BaseUuidModel, FormAsJSONModelMixin
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin

from edc_visit_tracking.model_mixins import CrfModelMixin as BaseCrfModelMixin
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin

from ..maternal_visit import MaternalVisit
from .consent_version_model_mixin import ConsentVersionModelModelMixin


class CrfModelMixin(ConsentVersionModelModelMixin, BaseCrfModelMixin,
                    SubjectScheduleCrfModelMixin,
                    RequiresConsentFieldsModelMixin, PreviousVisitModelMixin,
                    UpdatesCrfMetadataModelMixin, SiteModelMixin,
                    FormAsJSONModelMixin, ReferenceModelMixin, BaseUuidModel):

    """ Base model for all scheduled models
    """

    offschedule_compare_dates_as_datetimes = True
    maternal_visit = models.OneToOneField(MaternalVisit, on_delete=PROTECT)
    crf_date_validator_cls = None

    @property
    def subject_identifier(self):
        return self.maternal_visit.appointment.subject_identifier

    def natural_key(self):
        return self.maternal_visit.natural_key()

    natural_key.dependencies = ['td_maternal.maternalvisit']

    class Meta:
        abstract = True
