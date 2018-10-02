from django.db import models

from edc_constants.choices import YES_NO

from ..maternal_choices import SMOKING_DRINKING_FREQUENCY
from .model_mixins import CrfModelMixin


class MaternalSubstanceUseDuringPreg(CrfModelMixin):

    smoked_during_pregnancy = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Has the participant ever smoked cigarettes during this'
        ' pregnancy?  ',
    )

    smoking_during_preg_freq = models.CharField(
        max_length=30,
        choices=SMOKING_DRINKING_FREQUENCY,
        verbose_name='If yes, please indicate how much: ',
        blank=True,
        null=True,
    )

    alcohol_during_pregnancy = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Has the participant ever drank alcohol during this'
        ' pregnancy?',
    )

    alcohol_during_preg_freq = models.CharField(
        max_length=30,
        choices=SMOKING_DRINKING_FREQUENCY,
        verbose_name='If yes, please indicate how much: ',
        blank=True,
        null=True,
    )

    marijuana_during_preg = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Has the participant ever used marijuana during this'
        ' pregnancy?',
    )

    marijuana_during_preg_freq = models.CharField(
        max_length=30,
        choices=SMOKING_DRINKING_FREQUENCY,
        verbose_name='If yes, please indicate how much: ',
        blank=True,
        null=True,
    )

    other_illicit_substances_during_preg = models.TextField(
        max_length=500,
        verbose_name='Please list any other illicit substances that the'
        ' participant '
        'reports using during to this pregnancy.',
        blank=True,
        null=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = 'Maternal Substance Use During Pregnancy'
        verbose_name_plural = 'Maternal Substance Use During Pregnancy'
