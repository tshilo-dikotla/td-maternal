from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_consent.field_mixins import SampleCollectionFieldsMixin, VulnerabilityFieldsMixin
from edc_base.model_managers import HistoricalRecords
from edc_registration.models import RegisteredSubject


class SpecimenConsent(SampleCollectionFieldsMixin, RequiresConsentFieldsModelMixin,
                      VulnerabilityFieldsMixin, BaseUuidModel):

    """ A model completed by the user when a mother gives consent for specimen storage. """

    registered_subject = models.OneToOneField(
        RegisteredSubject, on_delete=PROTECT, null=True)

    history = HistoricalRecords()

    def __str__(self):
        return "{0}".format(self.registered_subject.subject_identifier)

    def natural_key(self):
        return self.registered_subject.natural_key()

    def prepare_appointments(self, using):
        """Overrides so that the signal does not attempt to prepare appointments."""
        pass

    def get_subject_identifier(self):
        return self.registered_subject.subject_identifier

    def get_report_datetime(self):
        return self.consent_datetime

    @property
    def subject_identifier(self):
        return self.get_subject_identifier()
#     subject_identifier.allow_tags = True

    @property
    def report_datetime(self):
        return self.consent_datetime

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Specimen Consent'
