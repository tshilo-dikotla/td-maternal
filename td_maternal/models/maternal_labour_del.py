from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel
from edc_protocol.validators import datetime_not_before_study_start
from edc_base.model_validators import datetime_not_future
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_registration.models import RegisteredSubject


from ..maternal_choices import DELIVERY_HEALTH_FACILITY, DELIVERY_MODE, CSECTION_REASON

from .list_models import DeliveryComplications


class MaternalLabourDel(BaseUuidModel):

    """ A model completed by the user on Maternal Labor and Delivery which triggers registration of infants. """

    registered_subject = models.OneToOneField(
        RegisteredSubject, on_delete=PROTECT, null=True)

    report_datetime = models.DateTimeField(
        verbose_name="Report date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        help_text='')

    delivery_datetime = models.DateTimeField(
        verbose_name="Date and time of delivery :",
        help_text="If TIME unknown, estimate",
        validators=[
            datetime_not_future, ])

    delivery_time_estimated = models.CharField(
        verbose_name="Is the delivery TIME estimated?",
        max_length=3,
        choices=YES_NO)

    delivery_hospital = models.CharField(
        verbose_name="Place of delivery? ",
        max_length=65,
        choices=DELIVERY_HEALTH_FACILITY,
        help_text="If 'OTHER', specify below")

    delivery_hospital_other = OtherCharField()

    labour_hrs = models.CharField(
        verbose_name="How long prior to to delivery, in HRS, did labour begin? ",
        max_length=10)

    mode_delivery = models.CharField(
        verbose_name="What was the mode of delivery?",
        max_length=100,
        choices=DELIVERY_MODE,
        help_text="If 'OTHER', specify below")

    mode_delivery_other = OtherCharField()

    csection_reason = models.CharField(
        verbose_name="If C-section was performed, indicate reason below",
        max_length=100,
        choices=CSECTION_REASON,
        help_text="If 'OTHER', specify below")

    csection_reason_other = OtherCharField()

    delivery_complications = models.ManyToManyField(
        DeliveryComplications,
        verbose_name="Were any of the following complications present at delivery? ",
        help_text="If 'OTHER', specify below")

    delivery_complications_other = OtherCharField()

    live_infants_to_register = models.IntegerField(
        verbose_name="How many babies are you registering to the study? ")

    still_births = models.IntegerField(
        default=0,
        verbose_name="How many still births or miscarriages?")

    valid_regiment_duration = models.CharField(
        verbose_name="(Interviewer) If HIV+ve, has the participant been on the ART "
                     "regimen for at least 4 weeks in pregnancy?",
        choices=YES_NO_NA,
        null=True,
        blank=False,
        max_length=15,
        help_text=("If not 4 or more weeks then participant will go OFF STUDY."))

    arv_initiation_date = models.DateField(
        verbose_name="(Interviewer) If on ART, when did the participant initiate therapy for this pregnancy?",
        null=True,
        blank=True)

    delivery_comment = models.TextField(
        verbose_name="List any additional information about the labour and delivery (mother only) ",
        max_length=250,
        blank=True,
        null=True)

    comment = models.TextField(
        verbose_name="Comment if any additional pertinent information ",
        max_length=250,
        blank=True,
        null=True)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        super(MaternalLabourDel, self).save(*args, **kwargs)

    def __str__(self):
        return "{0}".format(self.registered_subject.subject_identifier)

    def natural_key(self):
        return self.registered_subject.natural_key()
    natural_key.dependencies = ['edc_registration.registeredsubject']

    class Meta:
        app_label = 'td_maternal'
        verbose_name = "Delivery"
