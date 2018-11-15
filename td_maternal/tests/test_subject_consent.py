import re
from django.test import TestCase
from edc_base.utils import get_utcnow
from model_mommy import mommy

from ..models import SubjectConsent
subject_identifier = '092\-[0-9\-]+'


class TestSubjectConsent(TestCase):

    def setUp(self):
        self.subject_screening = mommy.make_recipe(
            'td_maternal.subjectscreening')

    def test_allocated_subject_identifier(self):
        """Test consent successfully allocates subject identifier on
        save.
        """
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        mommy.make_recipe('td_maternal.subjectconsent', **options)
        self.assertFalse(
            re.match(
                subject_identifier,
                SubjectConsent.objects.all()[0].subject_identifier))
