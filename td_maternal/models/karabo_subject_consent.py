from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_protocol.validators import datetime_not_before_study_start

ANSWERS = (
    ('Accepted', 'Yes and the client accepted the signed copy of the consent'),
    ('Refused', 'Yes and the client refused the signed copy of the consent'),
)


class KaraboSubjectConsent(SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    name = models.CharField(
        verbose_name='First Name',
        help_text=('(Must match name on file'
                   ' with Tshilo Dikotla Study)'),
        max_length=25
    )

    surname = models.CharField(
        verbose_name='Surname',
        help_text=('(Must match name on file '
                   'with Tshilo Dikotla Study)'),
        max_length=25
    )

    initials = models.CharField(
        verbose_name='Initials ',
        help_text=('(Must match initials on file '
                   'with Tshilo Dikotla Study)'),
        max_length=25
    )

    consent_lang = models.CharField(
        verbose_name='Language of consent:',
        max_length=25,
        choices=''
    )

    literacy = models.CharField(
        verbose_name='Is the participant literate?',
        max_length=25,
        choices=YES_NO
    )

    witness_name = models.DateTimeField(
        verbose_name='Witness’s first name and surname if '
        'participant is illiterate.',
        default=get_utcnow,
    )

    consent_datetime = models.DateTimeField(
        verbose_name='Consent date and time',
        default=get_utcnow,
        validators=[
            datetime_not_before_study_start,
            datetime_not_future]
    )

    omang = models.CharField(
        verbose_name='Omang of consenting woman',
        help_text=('(must match Omang on file with Tshilo Dikotla Study)'
                   ' (Confirm that all Tshilo Dikotla women have enrolled'
                   ' with an Omang, otherwise will need additional ID '
                   'questions.)'),
        max_length=25,
    )

    review = models.CharField(
        verbose_name='I have reviewed the Karabo study '
        'consent with the client.',
        max_length=25,
        choices=YES_NO
    )

    answer = models.CharField(
        verbose_name='I have answered all questions the client'
        ' had about the Karabo study consent.',
        max_length=25,
        choices=YES_NO
    )

    questions = models.CharField(
        verbose_name='I have asked the client questions'
        ' about the Karabo study and they have demonstrated an'
        ' understanding of the study by their answers.',
        max_length=25,
        choices=YES_NO
    )

    signed_consent = models.CharField(
        verbose_name='The client has signed the consent form.',
        max_length=25,
        choices=YES_NO
    )

    offer = models.CharField(
        verbose_name='I have offered the client a signed copy'
        ' of the consent form.',
        max_length=25,
        choices=ANSWERS
    )
