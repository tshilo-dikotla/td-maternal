from django.db import models
from edc_base.model_validators.date import date_not_future
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin


class MaternalRecontact(CrfModelMixin):

    contact_date = models.DateField(
        verbose_name='Date of contact',
        validators=[date_not_future])

    future_contact = models.CharField(
        verbose_name=('Does the participant agree to '
                      'be re-contacted for future studies?'),
        max_length=25,
        choices=YES_NO,
        help_text='If No, please give a reason below.')

    reason_no_contact = models.TextField(
        verbose_name=('If No, please give reason.'),
        max_length=250,
        blank=True,
        null=True)

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Maternal Re-contact'
