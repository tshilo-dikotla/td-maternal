from .model_mixins import UltraSoundModelMixin, CrfModelMixin


class MaternalUltraSoundFu(UltraSoundModelMixin, CrfModelMixin):

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Maternal Ultra Sound Follow Up'
