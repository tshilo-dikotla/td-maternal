from django.db import models
from edc_base.model_validators import date_not_future
from ..choices import ARV_DRUG_LIST, REASON_ARV_STOP
from .model_mixins import CrfModelMixin


class MaternalArv(CrfModelMixin):

    """ Inline ARV table to indicate ARV medication taken by mother """

    arv_code = models.CharField(
        verbose_name="ARV code",
        max_length=35,
        choices=ARV_DRUG_LIST,
        help_text='Regimen has to be at least 3.')

    start_date = models.DateField(
        verbose_name="Date Started",
        validators=[date_not_future],
        null=True,
        blank=False,
        help_text='WARNING: If date started is less than 4 weeks at delivery, '
        'complete off study.')

    stop_date = models.DateField(
        verbose_name="Date Stopped",
        null=True,
        blank=True)

    reason_for_stop = models.CharField(
        verbose_name="Reason for stop",
        choices=REASON_ARV_STOP,
        max_length=50,
        null=True,
        blank=True,
        help_text='If "Treatment Failure", notify study coordinator')

    reason_for_stop_other = models.TextField(
        max_length=250,
        verbose_name="Other, specify ",
        blank=True,
        null=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = 'Maternal ARV'
        verbose_name_plural = 'Maternal ARV'
