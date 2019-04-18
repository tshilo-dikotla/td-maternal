from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_appointment.models.appointment import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import NO, YES, NEG, POS, IND
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy


@tag('ae')
class TestAntenatalEnrollment(TestCase):

    def setUp(self):
        self.subject_screening = mommy.make_recipe(
            'td_maternal.subjectscreening')

        self.subject_consent = mommy.make_recipe(
            'td_maternal.tdconsentversion',
            screening_identifier=self.subject_screening.screening_identifier)

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

    def test_rapid_test_result_indeterminate_invalid_1(self):
        options = {
            'subject_identifier': self.subject_consent.subject_identifier,
            'report_datetime': get_utcnow(),
            'subject_identifier': self.subject_consent.subject_identifier,
            'rapid_test_date': get_utcnow().date() - relativedelta(days=3),
            'rapid_test_done': YES,
            'rapid_test_result': IND}
        self.antenatal_enrollment = mommy.make_recipe(
            'td_maternal.antenatalenrollment', **options)

        self.assertRaises(ValidationError, self.antenatal_enrollment.save())

    def test_rapid_test_result_change_invalid(self):
        options = {
            'subject_identifier': self.subject_consent.subject_identifier,
            'report_datetime': get_utcnow(),
            'subject_identifier': self.subject_consent.subject_identifier,
            'rapid_test_date': get_utcnow().date() - relativedelta(days=3),
            'rapid_test_done': YES,
            'rapid_test_result': NEG}
        self.antenatal_enrollment = mommy.make_recipe(
            'td_maternal.antenatalenrollment', **options)

        self.antenatal_enrollment.rapid_test_result = POS
        self.assertRaises(ValidationError, self.antenatal_enrollment.save())
