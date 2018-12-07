from django.db import models
from edc_base import get_utcnow
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_locator.models import SubjectLocator
from .model_mixins import CrfModelMixin


class MaternalLocator(SubjectLocator, CrfModelMixin):

    locator_date = models.DateField(
        default=get_utcnow().date(),
        verbose_name='Date Locator Form signed')

    health_care_infant = models.CharField(
        max_length=35,
        verbose_name=('Health clinic where your infant will'
                      ' receive their routine care'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Maternal Locator'
