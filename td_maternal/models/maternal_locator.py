from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_locator.models import SubjectLocator
from .model_mixins import CrfModelMixin


class MaternalLocator(SubjectLocator, CrfModelMixin):

    locator_date = models.DateField(
        verbose_name='Date Locator Form signed')

    health_care_infant = models.CharField(
        max_length=35,
        verbose_name=('Health clinic where your infant will'
                      ' receive their routine care'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Maternal Locator'
