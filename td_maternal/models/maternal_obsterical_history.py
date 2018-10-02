from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .model_mixins import CrfModelMixin


class MaternalObstericalHistory(CrfModelMixin):

    """ A model completed by the user on Obsterical History for all mothers.
    """

    prev_pregnancies = models.IntegerField(
        verbose_name='Including this pregnancy, how many previous pregnancies '
        'for this participant?',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    pregs_24wks_or_more = models.IntegerField(
        verbose_name='Number of pregnancies at least 24 weeks?',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    lost_before_24wks = models.IntegerField(
        verbose_name='Number of pregnancies lost before 24 weeks gestation',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    lost_after_24wks = models.IntegerField(
        verbose_name='Number of pregnancies lost at or after 24 weeks'
        ' gestation ',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    live_children = models.IntegerField(
        verbose_name='How many other living children does the participant'
        ' currently have (excluding baby to be enrolled in the study)',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    children_died_b4_5yrs = models.IntegerField(
        verbose_name='How many of the participant\'s children died after '
        'birth before 5 years of age? ',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    children_deliv_before_37wks = models.IntegerField(
        verbose_name='Number of previous prenancies delivered at < 37'
        ' weeks GA?',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    children_deliv_aftr_37wks = models.IntegerField(
        verbose_name='Number of previous prenancies delivered at >= 37'
        ' weeks GA?',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = 'Maternal Obsterical History'
