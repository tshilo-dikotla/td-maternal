from django.test import TestCase, tag
from ..models.eligibility import Eligibility
from edc_constants.constants import NO, YES


class TestEligibility(TestCase):

    """
    Participant age >= 18 is eligible else guardian must be present
    """
    @tag('valid_age_eligibility')
    def test_valid_age_eligibility(self):
        eligiblity = Eligibility(age_in_years=18, has_omang=YES)
        self.assertTrue(eligiblity.is_eligible)

    """Participant age < 18 are in eligible"""
    @tag('invalid_age_eligibility')
    def test_invalid_age_in_years_ineligibility(self):
        eligiblity = Eligibility(age_in_years=16, has_omang=YES)
        self.assertFalse(eligiblity.is_eligible)
        self.assertIn('Mother is under 18',
                      eligiblity.error_message)

    """Participant age > 50 are in eligible"""
    @tag('invalid_age_greater_eligibility')
    def test_age_in_years_greater_ineligibility(self):
        eligiblity = Eligibility(age_in_years=51, has_omang=YES)
        self.assertFalse(eligiblity.is_eligible)
        self.assertIn('Mother is too old (>50)',
                      eligiblity.error_message)

    """Participant who are not citizens are ineligible"""
    @tag('invalid_age_eligibility')
    def test_citizenship_ineligibility(self):
        eligiblity = Eligibility(age_in_years=16, has_omang=NO)
        self.assertFalse(eligiblity.is_eligible)
        self.assertIn('Mother is under 18',
                      eligiblity.error_message)
