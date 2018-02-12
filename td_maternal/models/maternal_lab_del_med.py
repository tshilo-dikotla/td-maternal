from django.db import models

from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO
from .model_mixins import CrfModelMixin


class MaternalLabDelMed(CrfModelMixin):

    """ Medical history collected during labor and delivery. """

    has_health_cond = models.CharField(
        verbose_name=(
            "Has the mother been newly diagnosed (during this pregnancy) "
            "with any major chronic health condition(s) that remain ongoing?"),
        max_length=3,
        choices=YES_NO)

    health_cond_other = OtherCharField()

    has_ob_comp = models.CharField(
        verbose_name=(
            "During this pregnancy, did the mother have any of the following "
            "obstetrical complications?"),
        max_length=3,
        choices=YES_NO)

    ob_comp_other = OtherCharField()

    took_supplements = models.CharField(
        verbose_name="Did the mother take any of the following medications during this pregnancy?",
        max_length=3,
        choices=YES_NO)

    supplements_other = OtherCharField()

    comment = models.TextField(
        verbose_name="Comment if any additional pertinent information ",
        max_length=250,
        blank=True,
        null=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = "Delivery: Medical"
        verbose_name_plural = "Delivery: Medical"
