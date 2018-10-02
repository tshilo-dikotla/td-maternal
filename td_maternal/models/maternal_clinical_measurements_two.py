from .model_mixins import CrfModelMixin
from .model_mixins import MaternalClinicalMeasurementsMixin


class MaternalClinicalMeasurementsTwo(
        CrfModelMixin, MaternalClinicalMeasurementsMixin):

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = 'Maternal Clinical Measurements Two'
        verbose_name_plural = 'Maternal Clinical Measurements Two'
