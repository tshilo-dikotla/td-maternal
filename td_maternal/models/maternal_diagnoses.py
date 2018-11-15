from .model_mixins import CrfModelMixin, DiagnosesMixin


class MaternalDiagnoses(CrfModelMixin, DiagnosesMixin):

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = "Maternal Diagnoses"
        verbose_name_plural = "Maternal Diagnosis"
