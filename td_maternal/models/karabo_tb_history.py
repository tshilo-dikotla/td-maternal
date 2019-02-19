from django.db import models
from edc_constants.choices import YES_NO_DONT_KNOW

from ..choices import FAMILY_RELATION
from .model_mixins import CrfModelMixin


class MaternalTuberculosisHistory(CrfModelMixin):
    """
    crf model about tuberculosis treatment history in family
    members relating to the infant
    """

    coughing = models.CharField(
        verbose_name=(
            'Since the last scheduled visit, has any member of the household where '
            'your has infant stayed been coughing for two weeks or more?'),
        max_length=3,
        choices=YES_NO_DONT_KNOW
    )

    coughing_rel = models.CharField(
        verbose_name=(
            'If yes to question 2, please indicate the relationship of this individual '
            'or individuals to your infant.'
        ),
        max_length=25,
        choices=FAMILY_RELATION
    )

    other_coughing_rel = models.CharField(
        verbose_name=('Other'),
        max_length=255,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    fever = models.CharField(
        verbose_name=(
            'Since the last scheduled visit, has any member of the household where your '
            'infant stayed had an unexplained fever concerning for tuberculosis?'),
        max_length=3,
        choices=YES_NO_DONT_KNOW
    )

    fever_rel = models.CharField(
        verbose_name=(
            'If yes to question 8, please indicate the relationship of the person '
            'or persons to the infant'),
        max_length=3,
        choices=FAMILY_RELATION
    )

    other_fever_rel = models.CharField(
        verbose_name=('Other'),
        max_length=255,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    weight_loss = models.CharField(
        verbose_name=(
            'Since the last attended scheduled visit has any member of the household '
            'where your infant stayed had any unexplained weight loss?'),
        max_length=3,
        choices=YES_NO_DONT_KNOW
    )

    weight_loss_rel = models.CharField(
        verbose_name=(
            'If yes to question 10, please indicate the relationship of the person '
            'or persons to the infant.'),
        max_length=3,
        choices=FAMILY_RELATION
    )

    other_weight_loss = models.CharField(
        verbose_name=('Other'),
        max_length=255,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    night_sweats = models.CharField(
        verbose_name=(
            'Since the last attended scheduled visit has any member of the household '
            'where your infant stayed had night sweats? An adult or child would be '
            'considered to have night sweats if they have had more than two nights of '
            'walking up with their night clothing drenched due to sweating with a '
            'need to change the night clothing.'),
        max_length=3,
        choices=YES_NO_DONT_KNOW
    )

    night_sweats_rel = models.CharField(
        verbose_name=(
            'If yes to question 12, please indicate the relationship of the '
            'person or persons to the infant'),
        max_length=3,
        choices=FAMILY_RELATION
    )

    other_night_sweats = models.CharField(
        verbose_name=('Other'),
        max_length=255,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    diagnosis = models.CharField(
        verbose_name=(
            'Since the last scheduled visit, has any member of the household where your '
            'infant has stayed been diagnosed with tuberculosis?'),
        max_length=3,
        choices=YES_NO_DONT_KNOW
    )

    diagnosis_rel = models.CharField(
        verbose_name=(
            'If yes to question 14, please indicate the relationship of the person '
            'or persons to the infant'),
        max_length=3,
        choices=FAMILY_RELATION
    )

    other_diagnosis_rel = models.CharField(
        verbose_name=('Other'),
        max_length=255,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    tb_exposure = models.CharField(
        verbose_name=(
            'Since the last attended scheduled visit do you have any reason to suspect '
            'your infant was exposed to tuberculosis outside of the household.'),
        max_length=3,
        choices=FAMILY_RELATION
    )

    tb_exposure_det = models.CharField(
        verbose_name=(
            'If yes to question 16, please comment on the nature'
            ' of the exposure'),
        max_length=255,
        help_text='please comment on the nature of the exposure',
        null=True,
        blank=True
    )
