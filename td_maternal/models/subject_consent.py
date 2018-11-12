from django.apps import apps as django_apps
from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.field_mixins import (
    CitizenFieldsMixin, VulnerabilityFieldsMixin)
from edc_consent.field_mixins import IdentityFieldsMixin
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.managers import ConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import (
    UpdatesOrCreatesRegistrationModelMixin)
from edc_search.model_mixins import SearchSlugManager

from edc_base.model_fields import OtherCharField

from ..maternal_choices import RECRUIT_SOURCE, RECRUIT_CLINIC
from .maternal_eligibility import MaternalEligibility
from .model_mixins import SearchSlugModelMixin


class SubjectConsentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class SubjectConsent(
        ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin,
        SiteModelMixin,
        NonUniqueSubjectIdentifierModelMixin, IdentityFieldsMixin,
        ReviewFieldsMixin, PersonalFieldsMixin, CitizenFieldsMixin,
        VulnerabilityFieldsMixin, SearchSlugModelMixin, BaseUuidModel):

    """ A model completed by the user on the mother's consent. """

    maternal_eligibility_model = 'td_maternal.maternaleligibility'

    screening_identifier = models.CharField(
        verbose_name='Screening identifier',
        max_length=50)

    recruit_source = models.CharField(
        max_length=75,
        choices=RECRUIT_SOURCE,
        verbose_name="The mother first learned about the tshilo "
        "dikotla study from ")

    recruit_source_other = OtherCharField(
        max_length=35,
        verbose_name="if other recruitment source, specify...",
        blank=True,
        null=True)

    recruitment_clinic = models.CharField(
        max_length=100,
        verbose_name="The mother was recruited from",
        choices=RECRUIT_CLINIC)

    recruitment_clinic_other = models.CharField(
        max_length=100,
        verbose_name="if other recruitment clinic, specify...",
        blank=True,
        null=True, )

    objects = SubjectConsentManager()

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def natural_key(self):
        return (self.subject_identifier, self.version)

    def get_maternal_eligibility(self):
        """Returns the maternal eligibility model instance.

        Instance must exist since MaternalEligibility is completed
        before consent.
        """
        model_cls = django_apps.get_model(self.maternal_eligibility_model)
        return model_cls.objects.get(
            screening_identifier=self.screening_identifier)

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Maternal Consent'
        unique_together = (('subject_identifier', 'version'),
                           ('subject_identifier', 'screening_identifier'),
                           ('first_name', 'dob', 'initials', 'version'))
