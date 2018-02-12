from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE

from ..choices import ARV_INTERRUPTION_REASON, ARV_DRUG_LIST, REASON_ARV_STOP
from .model_mixins import CrfModelMixin


class MaternalArvPreg(CrfModelMixin):

    """ This model is for all HIV positive mothers who are pregnant
    (whom we hope to enroll their infant) and/or for mothers who
    have just delivered
    """

    took_arv = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Did the mother receive any ARVs during this pregnancy?",
        help_text="(NOT including single -dose NVP in labour)")

    is_interrupt = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was there an interruption in the ARVs received during pregnancy through delivery of >/=3days?",
    )

    interrupt = models.CharField(
        verbose_name="Please give reason for interruption",
        max_length=50,
        choices=ARV_INTERRUPTION_REASON,
        default=NOT_APPLICABLE)

    interrupt_other = models.TextField(
        max_length=250,
        verbose_name="Other, specify ",
        blank=True,
        null=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = 'Maternal ARV In This Preg'
        verbose_name_plural = 'Maternal ARV In This Preg'


class MaternalArv(BaseUuidModel):

    """ Inline ARV table to indicate ARV medication taken by mother """

    maternal_arv_preg = models.ForeignKey(MaternalArvPreg, on_delete=PROTECT)

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
        help_text='WARNING: If date started is less than 4 weeks at delivery, complete off study.')

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

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Maternal ARV'
        verbose_name_plural = 'Maternal ARV'
        unique_together = (
            'maternal_arv_preg', 'arv_code', 'start_date', 'stop_date')
