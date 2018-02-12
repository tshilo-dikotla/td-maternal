# from django.db import models
#
# from edc_base.model_mixins import BaseUuidModel
# from edc_death_report.model_mixins import DeathReportModelMixin
#
# from .maternal_visit import MaternalVisit
#
#
# class MaternalDeathReport(DeathReportModelMixin, BaseUuidModel):
#
#     """ A model completed by the user on the mother's death. """
#
#     maternal_visit = models.OneToOneField(MaternalVisit)
#
#     class Meta:
#         app_label = 'td_maternal'
#         verbose_name = "Maternal Death Report"
