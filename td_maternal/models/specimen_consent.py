from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.field_mixins import (
    SampleCollectionFieldsMixin, VulnerabilityFieldsMixin)
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin


class SpecimenConsent(UniqueSubjectIdentifierFieldMixin,
                      SampleCollectionFieldsMixin,
                      RequiresConsentFieldsModelMixin, VulnerabilityFieldsMixin,
                      BaseUuidModel):

    """ A model completed by the user when a mother gives consent for specimen
     storage.
     """

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.subject_identifier}"

#     def natural_key(self):
#         return self.registered_subject.natural_key()

    def get_report_datetime(self):
        return self.consent_datetime

    @property
    def report_datetime(self):
        return self.consent_datetime

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Specimen Consent'
