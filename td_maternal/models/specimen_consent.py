from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_constants.choices import YES_NO, YES_NO_DECLINED
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_protocol.validators import datetime_not_before_study_start

from edc_consent.field_mixins import (
    SampleCollectionFieldsMixin, VulnerabilityFieldsMixin)
from edc_consent.field_mixins import ReviewFieldsMixin, VerificationFieldsMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_consent.validators import eligible_if_yes


class SpecimenConsent(UniqueSubjectIdentifierFieldMixin,
                      SampleCollectionFieldsMixin, ReviewFieldsMixin,
                      RequiresConsentFieldsModelMixin, VulnerabilityFieldsMixin,
                      VerificationFieldsMixin, SiteModelMixin, BaseUuidModel):

    """ A model completed by the user when a mother gives consent for specimen
     storage.
     """
    consent_datetime = models.DateTimeField(
        verbose_name='Consent date and time',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        help_text=('If reporting today, use today\'s date/time, otherwise use'
                   ' the date/time this information was reported.'))

    consent_reviewed = models.CharField(
        verbose_name=('I have explained the purpose of the specimen'
                      ' consent to the participant.'),
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        null=True,
        blank=False,
        help_text='If No the participant is not eligible.')

    assessment_score = models.CharField(
        verbose_name=(
            'To the best of my  knowledge, the client understands the purpose,'
            ' procedures, risks and benefits of the specimen consent:'),
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        null=True,
        blank=False)

    consent_copy = models.CharField(
        verbose_name=(
            'I offered the participant a copy of the signed specimen consent'
            ' and the participant accepted the copy:'),
        max_length=20,
        choices=YES_NO_DECLINED,
        null=True,
        blank=False,
        help_text=('If participant declined the copy, return the copy to the'
                   ' clinic to be filed with the original specimen consent'),
    )

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
