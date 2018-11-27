from edc_base.model_mixins import ListModelMixin
from edc_base.model_mixins import BaseUuidModel


class Contraceptives (ListModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'td_list'
        verbose_name = "Contraceptives"


verbose_name_plural = "Contraceptives"
