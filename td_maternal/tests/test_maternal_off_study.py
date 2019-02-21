from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy


@tag('offstudy')
class TestTDPrns(TestCase):

    def setUp(self):

        self.subject_screening = mommy.make_recipe(
            'td_maternal.subjectscreening')
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        self.subject_consent = mommy.make_recipe(
            'td_maternal.subjectconsent', **options)
        import_holidays()
        mommy.make_recipe(
            'td_maternal.antenatalenrollment', **options)

        self.appointments = Appointment.objects.filter(
            subject_identifier=self.subject_screening.screening_identifier)

    def test_subject_put_offstudy(self):
        print(self.appointments. subject_identifier,
              'self.subject_consent.version &&&&&&&&&&&&')
