from django.db import models
from django_crypto_fields.fields import EncryptedCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import CellNumber, TelephoneNumber
from edc_constants.choices import YES_NO
from edc_locator.models import SubjectLocator

from .model_mixins import CrfModelMixin


class MaternalLocator(SubjectLocator, CrfModelMixin):

    locator_date = models.DateField(
        verbose_name='Date Locator Form signed')

    health_care_infant = models.CharField(
        verbose_name=('Health clinic where your infant will'
                      ' receive their routine care'),
        max_length=35,
        blank=True,
        null=True)

    has_caretaker = models.CharField(
        verbose_name=(
            "Has the participant identified someone who will be "
            "responsible for the care of the baby in case of her death, to whom the "
            "study team could share information about her baby's health?"),
        max_length=25,
        choices=YES_NO,
        help_text="")

    caretaker_name = EncryptedCharField(
        verbose_name="Full Name of the responsible person",
        max_length=35,
        help_text="include firstname and surname",
        blank=True,
        null=True)

    caretaker_cell = EncryptedCharField(
        verbose_name="Cell number",
        max_length=8,
        validators=[CellNumber, ],
        blank=True,
        null=True)

    caretaker_tel = EncryptedCharField(
        verbose_name="Telephone number",
        max_length=8,
        validators=[TelephoneNumber, ],
        blank=True,
        null=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Maternal Locator'
