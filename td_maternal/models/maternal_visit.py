from django.db import models
from edc_appointment.models import Appointment
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_constants.constants import NOT_APPLICABLE
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.managers import VisitModelManager
from edc_visit_tracking.model_mixins import VisitModelMixin

from ..choices import VISIT_UNSCHEDULED_REASON, VISIT_REASON, VISIT_INFO_SOURCE


class MaternalVisit(
        VisitModelMixin, CreatesMetadataModelMixin,
        ReferenceModelMixin, RequiresConsentFieldsModelMixin,
        SiteModelMixin, BaseUuidModel):

    """ Maternal visit form that links all antenatal/ postnatal follow-up forms
    """

    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT)

    reason = models.CharField(
        verbose_name='What is the reason for this visit report?',
        max_length=25,
        choices=VISIT_REASON)

    reason_unscheduled = models.CharField(
        verbose_name=(
            'If \'Unscheduled\' above, provide reason for '
            'the unscheduled visit'),
        max_length=25,
        choices=VISIT_UNSCHEDULED_REASON,
        default=NOT_APPLICABLE)

    info_source = models.CharField(
        verbose_name='What is the main source of this information?',
        max_length=25,
        choices=VISIT_INFO_SOURCE)

    objects = VisitModelManager()

    history = HistoricalRecords()

    class Meta(VisitModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = 'Maternal Visit'
