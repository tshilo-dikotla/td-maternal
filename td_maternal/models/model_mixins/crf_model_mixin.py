from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_mixins import BaseUuidModel, FormAsJSONModelMixin
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin
from edc_visit_tracking.model_mixins import CrfModelMixin as BaseCrfModelMixin
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin

from edc_consent.model_mixins import RequiresConsentFieldsModelMixin

from ..maternal_visit import MaternalVisit


class CrfModelMixin(BaseCrfModelMixin, SubjectScheduleCrfModelMixin,
                    RequiresConsentFieldsModelMixin, PreviousVisitModelMixin,
                    UpdatesCrfMetadataModelMixin, SiteModelMixin,
                    FormAsJSONModelMixin, ReferenceModelMixin, BaseUuidModel):

    """ Base model for all scheduled models
    """

    offschedule_compare_dates_as_datetimes = True
    maternal_visit = models.OneToOneField(MaternalVisit, on_delete=PROTECT)

    def get_consent_version(self):
        subject_screening_cls = django_apps.get_model(
            'td_maternal.subjectscreening')
        consent_version_cls = django_apps.get_model(
            'td_maternal.tdconsentversion')
        try:
            subject_screening_obj = subject_screening_cls.objects.get(
                subject_identifier=self.maternal_visit.subject_identifier)
        except subject_screening_cls.DoesNotExist:
            raise ValidationError(
                'Missing Subject Screening form. Please complete '
                'it before proceeding.')
        else:
            try:
                consent_version_obj = consent_version_cls.objects.get(
                    screening_identifier=subject_screening_obj.screening_identifier)
            except consent_version_cls.DoesNotExist:
                raise ValidationError(
                    'Missing Consent Version form. Please complete '
                    'it before proceeding.')
            return consent_version_obj.version

    def save(self, *args, **kwargs):
        self.consent_version = self.get_consent_version()
        super(CrfModelMixin, self).save(*args, **kwargs)

    def natural_key(self):
        return self.maternal_visit.natural_key()
    natural_key.dependencies = ['td_maternal.maternalvisit']

    class Meta:
        abstract = True
