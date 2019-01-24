from .model_mixins import CrfModelMixin
from django.db import models
from edc_constants.choices import YES_NO_DONT_KNOW

from ..choices import FAMILY_RELATION


class MaternalTuberculosisHistory(CrfModelMixin):
    """
    crf model about tuberculosis treatment history in family
    members relating to the infant
    """

    coughing = models.CharField(
        verbose_name=('Since the last scheduled visit,'
                      ' has any member of the household where your has '
                      'infant stayed been coughing for two weeks or more?'),
        max_length=3,
        choices=YES_NO_DONT_KNOW
    )

    coughing_relation = models.CharField(
        verbose_name=('If yes to question 1, please indicate the relationship'
                      ' of this individual or individuals to your infant'
                      ),
        max_length=25,
        choices=FAMILY_RELATION
    )

    other_coughing_relation = models.CharField(
        verbose_name=('Other (Indicate Relationship:)'),
        max_length=255,
        null=True,
        blank=True
    )

    diagnosis = models.CharField(
        verbose_name=('Since the last scheduled visit, has any member of'
                      ' the household where your infant has stayed been'
                      ' diagnosed with tuberculosis?'),
        max_length=3,
        choices=YES_NO_DONT_KNOW
    )

    diagnosis_relation = models.CharField(
        verbose_name=('If yes to question 3, please indicate the relationship'
                      ' of this individual or individuals to your infant:'),
        max_length=3,
        choices=FAMILY_RELATION
    )

    other_diagnosis_relation = models.CharField(
        verbose_name=('Other (Indicate Relationship:)'),
        max_length=255,
        null=True,
        blank=True
    )

    tuberculosis_treatment = models.CharField(
        verbose_name=('Since the last scheduled visit, has any member of the'
                      ' household where your infant has stayed been treated '
                      'for tuberculosis?'),
        max_length=3,
        choices=YES_NO_DONT_KNOW
    )

    tuberculosis_treatment_relation = models.CharField(
        verbose_name=('If yes to question 5, please indicate the relationship'
                      ' of this individual or individuals to your infant:'),
        max_length=3,
        choices=FAMILY_RELATION
    )

    other_treatment_relation = models.CharField(
        verbose_name=('Other (Indicate Relationship:)'),
        max_length=255,
        null=True,
        blank=True
    )
