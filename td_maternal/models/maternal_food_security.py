from django.db import models
from edc_constants.choices import YES_NO_DONT_KNOW, YES_NO

from ..choices import OFTEN_SOMETIMES_NEVER_TRUE, SKIP_MEALS_FREQUEENCY
from .model_mixins import CrfModelMixin


class MaternalFoodSecurity(CrfModelMixin):

    """ A model completed by the user on the food eaten in the Mother's
     household in the last 2 weeks and whether they able to afford the food
     they need.
    """

    food_sufficient = models.CharField(
        verbose_name=('The first statement is, \'The food that (I/we) bought '
                      'just didn\'t last, and (I/we) didn\'t have money to '
                      'get more.\' Was that often, sometimes, or never true '
                      'for (you/your household) in the last 2 weeks?'),
        max_length=25,
        choices=OFTEN_SOMETIMES_NEVER_TRUE)

    balanced_meal = models.CharField(
        verbose_name=('\'(I/we) couldn’t afford to eat balanced meals.\' Was '
                      'that often, sometimes, or never true for (you/your '
                      'household) in the last 2 weeks?'),
        max_length=25,
        choices=OFTEN_SOMETIMES_NEVER_TRUE
    )

    skip_meals = models.CharField(
        verbose_name=('In the last 2 weeks, did (you/you or other adults in '
                      'your household) ever cut the size of your meals or '
                      'skip meals because there wasn\'t enough money for food?'),
        max_length=15,
        choices=YES_NO_DONT_KNOW,
    )

    skip_meals_frequency = models.CharField(
        verbose_name='In the last 2 weeks, how many days did this happen?',
        choices=SKIP_MEALS_FREQUEENCY,
        max_length=10,
        null=True,
        blank=True
    )

    eat_less = models.CharField(
        verbose_name=('In the last 2 weeks, did you ever eat less than you '
                      'felt you should because there wasn\'t enough money'
                      ' for food?'),
        max_length=15,
        choices=YES_NO_DONT_KNOW,
    )

    hungry = models.CharField(
        verbose_name=('In the last 2 weeks, were you ever hungry but didn\'t '
                      'eat because there wasn\'t enough money for food?'),
        max_length=15,
        choices=YES_NO_DONT_KNOW,
    )

    food_basket = models.CharField(
        verbose_name=('In the last 2 weeks, have you received a food basket '
                      'from the government?'),
        max_length=15,
        choices=YES_NO,
    )

    additional_comments = models.TextField(
        max_length=50,
        null=True,
        blank=True
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = 'Maternal Food Security'
        verbose_name_plural = 'Maternal Food Security'
