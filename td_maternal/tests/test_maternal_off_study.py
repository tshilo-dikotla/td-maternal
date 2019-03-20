from dateutil.relativedelta import relativedelta
from edc_appointment.constants import IN_PROGRESS_APPT
from edc_appointment.models.appointment import Appointment
from edc_base.utils import get_utcnow
from model_mommy import mommy

from .base_test_case import BaseTestCase


class TestTDOffStudy(BaseTestCase):

    def setUp(self):
        super(TestTDOffStudy, self).setUp()
        options = {
            'screening_identifier': '12345',
            'consent_datetime': get_utcnow,
            'subject_identifier': '123456789'}

        self.subject_consent = mommy.make_recipe(
            'td_maternal.subjectconsent', **options)

        options = {**self.hiv_pos_mother_options(),
                   'report_datetime': get_utcnow() - relativedelta(days=3)}
        self.create_mother(options, report_datetime=get_utcnow(
        ) - relativedelta(days=3))

        mommy.make_recipe(
            'td_maternal.maternaloffstudy',
            subject_identifier=self.subject_consent.subject_identifier,
            offstudy_date=get_utcnow().date() - relativedelta(days=2),
            report_datetime=get_utcnow() - relativedelta(days=2),
            offschedule_datetime=get_utcnow() - relativedelta(days=2),
            reason='multiple_vialble_gestations')

    def test_subject_put_offstudy(self):

        appointments = Appointment.objects.filter(
            subject_identifier=self.subject_consent.subject_identifier,
            appt_status=IN_PROGRESS_APPT)

        self.assertEqual(appointments.count(), 0)

        appointment = Appointment.objects.filter(
            subject_identifier=self.subject_consent.subject_identifier).first()

        appointment.appt_status = IN_PROGRESS_APPT
        appointment.save()
