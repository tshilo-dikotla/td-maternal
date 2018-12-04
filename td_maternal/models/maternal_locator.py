from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_locator.models import SubjectLocator


class MaternalLocator(SubjectLocator, BaseUuidModel):

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Maternal Locator'
