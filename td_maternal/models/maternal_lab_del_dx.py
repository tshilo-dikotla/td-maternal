from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO, YES_NO_NA
from .model_mixins import CrfModelMixin
from ..choices import DX_MATERNAL


class MaternalLabDelDx(CrfModelMixin):

    """ Diagnosis during pregnancy collected during labor and delivery.
    This is for HIV positive mothers only"""

    has_who_dx = models.CharField(
        verbose_name=(
            'During this pregnancy, did the mother have any new diagnoses '
            'listed in the WHO Adult/Adolescent HIV clinical staging document'
            'which is/are NOT reported?'),
        max_length=3,
        choices=YES_NO_NA)

    has_preg_dx = models.CharField(
        verbose_name='During this pregnancy, did the mother have any '
        'of the following diagnoses?',
        max_length=3,
        choices=YES_NO,
        help_text='If yes, Select all that apply in the table, '
        'only report grade 3 or 4 diagnoses')

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = "Delivery: Preg Dx"


class MaternalLabDelDxT(BaseUuidModel):

    """ Inline diagnosis during pregnancy collected during
    labor and delivery (transactions).
    """

    maternal_lab_del_dx = models.OneToOneField(MaternalLabDelDx)

    lab_del_dx = models.CharField(
        verbose_name="Diagnosis",
        max_length=175,
        choices=DX_MATERNAL)

    lab_del_dx_specify = models.CharField(
        verbose_name="Diagnosis specification",
        max_length=50,
        blank=True,
        null=True)

    grade = models.IntegerField(
        verbose_name="Grade")

    hospitalized = models.CharField(
        verbose_name="Hospitalized",
        max_length=3,
        choices=YES_NO)

    class Meta:
        app_label = 'td_maternal'
        verbose_name = "Delivery: Preg DxT"
