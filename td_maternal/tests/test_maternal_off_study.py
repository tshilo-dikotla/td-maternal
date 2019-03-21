from dateutil.relativedelta import relativedelta
from django.test import tag
from edc_appointment.constants import IN_PROGRESS_APPT
from edc_appointment.models.appointment import Appointment
from edc_base.utils import get_utcnow
from edc_metadata.constants import REQUIRED
from edc_metadata.models import CrfMetadata, RequisitionMetadata
from model_mommy import mommy

from .base_test_case import BaseTestCase


@tag('offstudy')
class TestTDOffStudy(BaseTestCase):

    def setUp(self):
        super(TestTDOffStudy, self).setUp()

        options = {**self.hiv_pos_mother_options(),
                   'report_datetime': get_utcnow() - relativedelta(days=3)}
        self.create_mother(options, report_datetime=get_utcnow(
        ) - relativedelta(days=3))

    def test_subject_put_offstudy(self):

        mommy.make_recipe(
            'td_maternal.maternaloffstudy',
            subject_identifier=self.subject_consent.subject_identifier,
            offstudy_date=get_utcnow().date() - relativedelta(days=2),
            report_datetime=get_utcnow() - relativedelta(days=2),
            offschedule_datetime=get_utcnow() - relativedelta(days=2),
            reason='multiple_vialble_gestations')

        appointments = Appointment.objects.filter(
            subject_identifier=self.subject_consent.subject_identifier,
            appt_status=IN_PROGRESS_APPT)

        self.assertEqual(appointments.count(), 0)

    def test_maternal_ultrasound_multiple_gestations(self):
        self.maternal_ultrasound_initial.number_of_gestations = 2
        self.maternal_ultrasound_initial.save()

        crfs = CrfMetadata.objects.filter(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1000M')

        for crf in crfs:
            self.assertNotEqual(
                crf.entry_status, REQUIRED)
