from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from django_crypto_fields.fields import (
    FirstnameField, LastnameField, EncryptedCharField,
    IdentityField)
from django_crypto_fields.mixins import CryptoMixin
from edc_base.model_fields import IsDateEstimatedField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_base.sites import CurrentSiteManager
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_protocol.validators import datetime_not_before_study_start

from edc_consent.field_mixins import VerificationFieldsMixin
from edc_consent.validators import FullNameValidator

from ..choices import ANSWERS


class KaraboSubjectConsentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier, screening_identifier):
        return self.get(
            subject_identifier=subject_identifier, screening_identifier=screening_identifier)


class KaraboSubjectConsent(CryptoMixin, VerificationFieldsMixin,
                           SiteModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    screening_identifier = models.CharField(
        verbose_name="Screening Identifier",
        max_length=36,
        unique=True)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    first_name = FirstnameField(
        verbose_name='First Name',
        help_text=('(Must match name on file'
                   ' with Tshilo Dikotla Study)'))

    last_name = LastnameField(
        verbose_name='Surname',
        help_text=('(Must match name on file '
                   'with Tshilo Dikotla Study)'))

    initials = EncryptedCharField(
        verbose_name='Initials ',
        help_text=('(Must match initials on file '
                   'with Tshilo Dikotla Study)'))

    dob = models.DateField(
        verbose_name="Date of birth",
        null=True,
        blank=False)

    is_dob_estimated = IsDateEstimatedField(
        verbose_name="Is date of birth estimated?",
        null=True,
        blank=False)

    language = models.CharField(
        verbose_name='Language of consent:',
        max_length=25,
        choices=settings.LANGUAGES)

    is_literate = models.CharField(
        verbose_name='Is the participant literate?',
        max_length=25,
        choices=YES_NO)

    guardian_name = LastnameField(
        verbose_name='Witness\'s last and first name',
        validators=[FullNameValidator()],
        blank=True,
        null=True,
        help_text=mark_safe(
            'Required only if participant is illiterate.<br>'
            'Format is \'LASTNAME, FIRSTNAME\'. '
            'All uppercase separated by a comma.'))

    consent_datetime = models.DateTimeField(
        verbose_name='Consent date and time',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future])

    identity = IdentityField(
        verbose_name='Omang of consenting woman',
        help_text=mark_safe('(must match Omang on file '
                            'with Tshilo Dikotla Study)'
                            ' (Confirm that all Tshilo Dikotla '
                            'women have enrolled with an Omang, '
                            'otherwise will need additional ID '
                            'questions.)'))

    consent_reviewed = models.CharField(
        verbose_name='I have reviewed the Karabo study '
        'consent with the client.',
        max_length=3,
        choices=YES_NO)

    study_questions = models.CharField(
        verbose_name='I have answered all questions the client'
        ' had about the Karabo study consent.',
        max_length=3,
        choices=YES_NO)

    assessment_score = models.CharField(
        verbose_name='I have asked the client questions'
        ' about the Karabo study and they have demonstrated an'
        ' understanding of the study by their answers.',
        max_length=3,
        choices=YES_NO)

    consent_signature = models.CharField(
        verbose_name='The client has signed the consent form.',
        max_length=3,
        choices=YES_NO)

    consent_copy = models.CharField(
        verbose_name='I have offered the client a signed copy'
        ' of the consent form.',
        max_length=25,
        choices=ANSWERS)

    def __str__(self):
        return f'{self.subject_identifier} {self.screening_identifier}'

    def natural_key(self):
        return (self.subject_identifier, self.screening_identifier)

    objects = KaraboSubjectConsentManager()

    history = HistoricalRecords()

    on_site = CurrentSiteManager()

    class Meta:
        app_label = 'td_maternal'
        verbose_name = "Karabo Subject Consent"
        verbose_name_plural = "Karabo Subject Consents"
