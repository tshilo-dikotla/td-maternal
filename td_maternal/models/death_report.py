from django.core.validators import MinValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import datetime_not_future
from edc_base.model_fields import OtherCharField
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_protocol.validators import datetime_not_before_study_start

from ..choices import (CAUSE_OF_DEATH, TB_SITE_DEATH,
                       SOURCE_OF_DEATH_INFO, CAUSE_OF_DEATH_CAT, MED_RESPONSIBILITY,
                       HOSPITILIZATION_REASONS)
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

    primary_source = models.CharField(
        max_length=100,
        choices=SOURCE_OF_DEATH_INFO,
        verbose_name='what is the primary source of'
        ' cause of death information?')

    primary_source_other = OtherCharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If "Other" above, please specify')

    cause_of_death = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH,
        verbose_name=('Main cause of death'),
        help_text=('Main cause of death in the opinion of the '
                   ' local study doctor and local PI'))

    cause_of_death_other = OtherCharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If "Other" above, please specify')

    cause_category = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH_CAT,
        verbose_name='based on the narrative, what category best defines'
        ' the major cause of death?')

    cause_category_other = OtherCharField(
        verbose_name='If "Other" above, please specify',
        blank=True,
        null=True)

    tb_site = models.CharField(
        verbose_name='If cause of death is TB, specify site of TB disease',
        max_length=25,
        choices=TB_SITE_DEATH,
        default=NOT_APPLICABLE)

    perform_autopsy = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Will an autopsy be performed later')

    medical_responsibility = models.CharField(
        choices=MED_RESPONSIBILITY,
        max_length=50,
        verbose_name='Who was responsible for primary medical care of the '
        'participant during the month prior to death?',
        help_text="")

    participant_hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was the participant hospitalised before death?")

    reason_hospitalized = models.CharField(
        choices=HOSPITILIZATION_REASONS,
        max_length=50,
        verbose_name="if yes, hospitalized, what was the primary reason for hospitalisation? ",
        help_text="",
        blank=True,
        null=True)

    reason_hospitalized_other = models.TextField(
        verbose_name='if other illness or pathogen specify or non '
        'infectious reason, please specify below:',
        max_length=250,
        blank=True,
        null=True)

    days_hospitalized = models.IntegerField(
        verbose_name=(
            'For how many days was the participant hospitalised during '
            'the illness immediately before death? '),
        help_text="in days",
        default=0)

    narrative = models.TextField(
        verbose_name=(
            'Describe the major cause of death (including pertinent autopsy information '
            'if available), starting with the first noticeable illness thought to be '
            'related to death, continuing to time of death.'),
        help_text=(
            'Note: Cardiac and pulmonary arrest are not major reasons and should not '
            'be used to describe major cause'))

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier, )
    natural_key.dependencies = ['sites.Site']

    class Meta:
        verbose_name = 'Maternal Death Report'
