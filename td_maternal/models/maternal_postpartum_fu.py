from django.core.validators import MinValueValidator
from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO

from .model_mixins import DiagnosesMixin, CrfModelMixin
from .list_models import MaternalHospitalization


class MaternalPostPartumFu(CrfModelMixin, DiagnosesMixin):

    hospitalized = models.CharField(
        max_length=25,
        verbose_name="Has the mother been hospitalized since the last study visit?",
        choices=YES_NO,
        help_text="",
    )

    hospitalization_reason = models.ManyToManyField(
        MaternalHospitalization,
        verbose_name="Was the hospitalization for any of the following reasons?",
        blank=True,
        help_text="",
    )

    hospitalization_reason_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True,
    )

    hospitalization_days = models.IntegerField(
        verbose_name="How many days was the mother hospitalized?",
        validators=[MinValueValidator(1)],
        blank=True,
        null=True,
        help_text=""
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = "Maternal Post Partum Fu"
