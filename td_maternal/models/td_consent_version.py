from django.db import models

# from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_protocol.validators import date_not_before_study_start
from .subject_screening import SubjectScreening
from ..choices import CONSENT_VERSION
from django.db.models.deletion import PROTECT
from td_maternal.models.model_mixins.crf_model_mixin import CrfModelMixin


class TdConsentVersion(CrfModelMixin):

    subjectscreening = models.ForeignKey(
        SubjectScreening, null=True, on_delete=PROTECT)

    version = models.CharField(
        verbose_name="Which version of the consent would you like to be consented with.",
        choices=CONSENT_VERSION,
        max_length=3)

    report_datetime = models.DateField(
        verbose_name="Report datetime.",
        validators=[
            date_not_before_study_start,
            date_not_future, ],
        null=True,
        blank=True)

#     def __str__(self):
#         return str(self.maternal_eligibility.age_in_years) + str(self.version)
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.modified = self.created
#         super(TdConsentVersion, self).save(*args, **kwargs)

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'TD Consent Version'
        verbose_name_plural = 'TD Consent Version'
#         unique_together = ('maternal_eligibility', 'version')
