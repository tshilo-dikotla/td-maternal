from django.conf import settings
from django.db import models
from django_crypto_fields.mixins import CryptoMixin
from django_crypto_fields.fields import (
    FirstnameField, LastnameField, EncryptedCharField,
    IdentityField)
from django.utils.safestring import mark_safe

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_consent.validators import FullNameValidator

from edc_protocol.validators import datetime_not_before_study_start

from ..choices import ANSWERS


class KaraboSubjectConsent(CryptoMixin, SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    name = FirstnameField(
        verbose_name='First Name',
        help_text=('(Must match name on file'
                   ' with Tshilo Dikotla Study)'))

    surname = LastnameField(
        verbose_name='Surname',
        help_text=('(Must match name on file '
                   'with Tshilo Dikotla Study)'))

    initials = EncryptedCharField(
        verbose_name='Initials ',
        help_text=('(Must match initials on file '
                   'with Tshilo Dikotla Study)'))

    consent_lang = models.CharField(
        verbose_name='Language of consent:',
        max_length=25,
        choices=settings.LANGUAGES)

    literacy = models.CharField(
        verbose_name='Is the participant literate?',
        max_length=25,
        choices=YES_NO)

    witness_name = LastnameField(
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

    omang = IdentityField(
        verbose_name='Omang of consenting woman',
        help_text=mark_safe('(must match Omang on file '
                            'with Tshilo Dikotla Study)'
                            ' (Confirm that all Tshilo Dikotla '
                            'women have enrolled with an Omang, '
                            'otherwise will need additional ID '
                            'questions.)'))

    review = models.CharField(
        verbose_name='I have reviewed the Karabo study '
        'consent with the client.',
        max_length=3,
        choices=YES_NO)

    answer = models.CharField(
        verbose_name='I have answered all questions the client'
        ' had about the Karabo study consent.',
        max_length=3,
        choices=YES_NO)

    questions = models.CharField(
        verbose_name='I have asked the client questions'
        ' about the Karabo study and they have demonstrated an'
        ' understanding of the study by their answers.',
        max_length=3,
        choices=YES_NO)

    signed_consent = models.CharField(
        verbose_name='The client has signed the consent form.',
        max_length=3,
        choices=YES_NO)

    offer = models.CharField(
        verbose_name='I have offered the client a signed copy'
        ' of the consent form.',
        max_length=25,
        choices=ANSWERS)

    class Meta:
        app_label = 'td_maternal'
        verbose_name = "Karabo Subject Consent"
        verbose_name_plural = "Karabo Subject Consents"
