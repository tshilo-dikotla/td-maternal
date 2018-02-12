from django.db import models
from django.utils import timezone
from django.db.models.deletion import PROTECT

from django_crypto_fields.fields import EncryptedCharField
from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import CellNumber, TelephoneNumber
from edc_base.model_validators import datetime_not_future
from edc_constants.choices import YES_NO
from edc_locator.model_mixins import LocatorModelMixin
from edc_protocol.validators import datetime_not_before_study_start
from edc_registration.models import RegisteredSubject


class MaternalLocator(LocatorModelMixin, BaseUuidModel):

    """ A model completed by the user to capture locator information and
    the details of the infant caretaker. """

    registered_subject = models.OneToOneField(
        RegisteredSubject, on_delete=PROTECT, null=True)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        default=timezone.now,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    care_clinic = OtherCharField(
        verbose_name="Health clinic where your infant will receive their routine care ",
        max_length=35,
    )

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

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Maternal Locator'
