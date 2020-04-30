from django.db import models
from edc_base.model_validators.date import date_not_future
from edc_constants.choices import YES_NO, YES_NO_UNKNOWN

from edc_action_item.model_mixins.action_model_mixin import ActionModelMixin

from ..action_items import MATERNAL_COVID_SCREENING_ACTION
from ..choices import YES_NO_TRIED, POS_NEG_PENDING
from .list_models import CovidSymptoms
from .model_mixins import CrfModelMixin


class MaternalCovidScreening(ActionModelMixin, CrfModelMixin):

    tracking_identifier_prefix = 'MC'

    action_name = MATERNAL_COVID_SCREENING_ACTION

    covid_tested = models.CharField(
        verbose_name='Have you been tested for COVID-19?',
        max_length=10,
        choices=YES_NO_TRIED)

    covid_test_date = models.DateField(
        verbose_name="Date of test",
        validators=[date_not_future],
        null=True,
        blank=True)

    is_test_date_estimated = models.CharField(
        verbose_name="Is this an estimated date?",
        max_length=3,
        choices=YES_NO,
        null=True,
        blank=True)

    covid_results = models.CharField(
        verbose_name='What was the result of the test?',
        max_length=17,
        choices=POS_NEG_PENDING,
        null=True,
        blank=True)

    household_positive = models.CharField(
        verbose_name=('Has anyone in your household tested positive '
                      'for COVID-19'),
        max_length=3,
        choices=YES_NO_UNKNOWN)

    household_test_date = models.DateField(
        verbose_name="Date of test",
        validators=[date_not_future],
        null=True,
        blank=True)

    is_household_test_estimated = models.CharField(
        verbose_name="Is this an estimated date?",
        max_length=3,
        choices=YES_NO,
        null=True,
        blank=True)

    covid_contact = models.CharField(
        verbose_name=('Have you been in close contact with anyone outside of '
                      'your household who tested positive for COVID-19?'),
        max_length=3,
        choices=YES_NO_UNKNOWN)

    covid_symptoms = models.ManyToManyField(
        CovidSymptoms,
        verbose_name='In the last 14 days, have you experienced')

    comments = models.TextField(
        max_length=150,
        null=True,
        blank=True)

    @property
    def subject_identifier(self):
        return self.maternal_visit.subject_identifier

    class Meta:
        app_label = 'td_maternal'
