import re

from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_registration.models import RegisteredSubject
from model_mommy import mommy

from ..models import SubjectConsent, SubjectScreening


subject_identifier = '092\-[0-9\-]+'


@tag('cs')
class TestSubjectConsent(TestCase):

    def setUp(self):
        self.subject_screening = mommy.make_recipe(
            'td_maternal.subjectscreening')
        self.subject_consent = mommy.make_recipe(
            'td_maternal.tdconsentversion',
            screening_identifier=self.subject_screening.screening_identifier)

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

    def test_update_subject_identifier_on_screening(self):
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        subject_consent = mommy.make_recipe(
            'td_maternal.subjectconsent', **options)
        subject_screening = SubjectScreening.objects.get(
            screening_identifier=self.subject_screening.screening_identifier)
        self.assertEqual(
            subject_screening.subject_identifier,
            subject_consent.subject_identifier)

    def test_create_registered_subject(self):
        """Test if registered subject is created.
        """
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        subject_consent = mommy.make_recipe(
            'td_maternal.subjectconsent', **options)
        try:
            RegisteredSubject.objects.get(
                subject_identifier=subject_consent.subject_identifier)
        except RegisteredSubject.DoesNotExist:
            raise ValidationError('Registered subject is expected.')
        self.assertEqual(RegisteredSubject.objects.all().count(), 1)
