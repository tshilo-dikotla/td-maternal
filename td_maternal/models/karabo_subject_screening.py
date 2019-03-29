from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_protocol.validators import datetime_not_before_study_start


class KaraboSubjectScreening(SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    infant_alive = models.CharField(
        verbose_name='Has this woman given birth to a live born infant'
        ' that has been enrolled in the Tshilo Dikotla ',
        choices=YES_NO,
        max_length=25
    )

    infant_weight = models.CharField(
        verbose_name='Did the infant have a birth weight of ≥ 2.00 kilograms?',
        choices=YES_NO,
        max_length=25
    )

    major_anomalies = models.CharField(
        verbose_name='Was this infant born with any major congenital anomalies',
        choices=YES_NO,
        max_length=25
    )

    birth_complications = models.CharField(
        verbose_name='Did this infant experience any severe birth complications'
        ' such as birth asphyxia or seizures?',
        choices=YES_NO,
        max_length=25
    )

    infant_documentation = models.CharField(
        verbose_name='Does the infant have documentation that they received a '
        'BCG vaccine within 72 hours of birth in the Under 5 Health Booklet?',
        choices=YES_NO,
        max_length=25
    )

    infant_months = models.CharField(
        verbose_name='Has the infant reached 14 months of age or has the '
        'infant already attended the 12 month Tshilo Dikotla Study visit?',
        choices=YES_NO,
        max_length=25
    )

    tb_treatment = models.CharField(
        verbose_name='Was this woman being treated for tuberculosis in '
        'pregnancy or at the time she delivered the infant enrolled in '
        'the Tshilo Dikotla Study?',
        choices=YES_NO,
        max_length=25
    )

    incarcerated = models.CharField(
        verbose_name='Is this woman currently incarcerated?',
        max_length=25,
        choices=YES_NO
    )

    willing_to_consent = models.CharField(
        verbose_name='Is the woman willing to provide informed consent'
        ' to participate in the Karabo study?',
        max_length=25,
        choices=YES_NO
    )

