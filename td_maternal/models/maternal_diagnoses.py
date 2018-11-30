from .model_mixins import CrfModelMixin, DiagnosesMixin


class MaternalDiagnoses(CrfModelMixin, DiagnosesMixin):

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = "Maternal Diagnosis"
        verbose_name_plural = "Maternal Diagnoses"
