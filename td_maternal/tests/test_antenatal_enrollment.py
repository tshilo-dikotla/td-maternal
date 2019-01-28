from django.test import TestCase
from model_mommy import mommy

from edc_appointment.models.appointment import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import NO
from edc_facility.import_holidays import import_holidays

from ..models import AntenatalEnrollmentEligibility


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
        print(self.subject_consent.version,
              'self.subject_consent.version &&&&&&&&&&&&')
        mommy.make_recipe(
            'td_maternal.antenatalenrollment', **options)
        appointments = Appointment.objects.filter(
            subject_identifier=self.subject_consent.subject_identifier)
        for ap in appointments:
            print(ap.schedule_name, ap.subject_identifier, ap)

    def test_antenatal_enrollment_eligibility(self):
        antenatal_eligibility = AntenatalEnrollmentEligibility()
        pass

    def test_participant_ineligible(self):
        """Test if appointments are not created if participant is not eligible.
        """
        options = {
            'subject_identifier': self.subject_consent.subject_identifier,
            'will_breastfeed': NO}
        mommy.make_recipe(
            'td_maternal.antenatalenrollment', **options)
        appointments = Appointment.objects.filter(
            subject_identifier=self.subject_consent.subject_identifier)
        self.assertEqual(appointments.count(), 0)
