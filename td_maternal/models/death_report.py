from django.core.validators import MinValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_protocol.validators import datetime_not_before_study_start

from ..choices import CAUSE_OF_DEATH, TB_SITE_DEATH
from .model_mixins import CrfModelMixin


class DeathReport(CrfModelMixin, UniqueSubjectIdentifierFieldMixin):

    report_datetime = models.DateTimeField(
        verbose_name='Report Date',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow)

    death_datetime = models.DateTimeField(
        validators=[datetime_not_future],
        verbose_name='Date and Time of Death')

    study_day = models.IntegerField(
        validators=[MinValueValidator(1), ],
        verbose_name='Study day')

    death_as_inpatient = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Death as inpatient')

    cause_of_death = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH,
        verbose_name=('Main cause of death'),
        help_text=('Main cause of death in the opinion of the '
                   'local study doctor and local PI'))

    cause_of_death_other = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If "Other" above, please specify')

    tb_site = models.CharField(
        verbose_name='If cause of death is TB, specify site of TB disease',
        max_length=25,
        choices=TB_SITE_DEATH,
        default=NOT_APPLICABLE)

    narrative = models.TextField(
        verbose_name='Narrative')

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier, )
    natural_key.dependencies = ['sites.Site']

    class Meta:
        verbose_name = 'Maternal Death Report'
