from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .model_mixins import CrfModelMixin
from .model_mixins import MaternalClinicalMeasurementsMixin


class MaternalClinicalMeasurementsOne(CrfModelMixin, MaternalClinicalMeasurementsMixin):

    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Mother's height? ",
        validators=[MinValueValidator(114), MaxValueValidator(195), ],
        help_text="Measured in Centimeters (cm)")

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = 'Maternal Clinical Measurements One'
        verbose_name_plural = 'Maternal Clinical Measurements One'
