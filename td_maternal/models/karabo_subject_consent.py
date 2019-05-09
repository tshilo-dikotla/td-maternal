from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.safestring import mark_safe
from django_crypto_fields.fields import (
    FirstnameField, LastnameField, EncryptedCharField,
    IdentityField)
from django_crypto_fields.mixins import CryptoMixin
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_protocol.validators import datetime_not_before_study_start

from edc_consent.validators import FullNameValidator

from ..choices import ANSWERS


class KaraboSubjectConsent(CryptoMixin, SiteModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    screening_identifier = models.CharField(
        verbose_name="Screening Identifier",
        max_length=36,
        unique=True)

    maternal_subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

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
        default=get_utcnow,
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

    def get_karabo_eligibility(self):
        """Returns the maternal eligibility model instance.
           Instance must exist since MaternalEligibility is completed
           before consent.
        """
        model_cls = django_apps.get_model('td_infant.karabosubjectscreening')
        try:
            karabo_model_obj = model_cls.objects.get(
                screening_identifier=self.screening_identifier)
        except model_cls.DoesNotExist:
            raise ValidationError(
                f'Missing Karabo Screening.')
        else:
            return karabo_model_obj

    def save(self, *args, **kwargs):
        self.maternal_subject_identifier = self.subject_identifier[:-3]
        super(KaraboSubjectConsent, self).save(*args, **kwargs)

    class Meta:
        app_label = 'td_infant'
        verbose_name = "Karabo Subject Consent"
        verbose_name_plural = "Karabo Subject Consents"
