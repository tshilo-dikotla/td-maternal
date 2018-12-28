from django.test import TestCase
from model_mommy import mommy

from edc_appointment.models.appointment import Appointment
from edc_base.utils import get_utcnow
from edc_facility.import_holidays import import_holidays


class TestAntenatalEnrollment(TestCase):

    def setUp(self):
        self.subject_screening = mommy.make_recipe(
            'td_maternal.subjectscreening')
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        self.subject_consent = mommy.make_recipe(
            'td_maternal.subjectconsent', **options)
        import_holidays()

    def test_create_appointments(self):
        """Test if appointments are created.
        """
        options = {
            'subject_identifier': self.subject_consent.subject_identifier}
        mommy.make_recipe(
            'td_maternal.antenatalenrollment', **options)
        appointments = Appointment.objects.filter(
            subject_identifier=self.subject_consent.subject_identifier)
        self.assertEqual(appointments.count(), 1)
