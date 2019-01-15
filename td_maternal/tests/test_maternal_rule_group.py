from django.test import tag
from edc_metadata.constants import REQUIRED, NOT_REQUIRED
from edc_metadata.models import CrfMetadata

from .base_test_case import BaseTestCase


@tag('m_rule')
class TestMaternalRuleGroup(BaseTestCase):

    def setUp(self):
        super(TestMaternalRuleGroup, self).setUp()

    def test_maternalarvpreg_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        print('>>>>>>>', CrfMetadata.objects.get(
            model='td_maternal.maternalarvpreg',
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1000M').__dict__)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalarvpreg',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1000M').entry_status, REQUIRED)

    def test_maternalarvpreg_not_required(self):
        self.create_mother(self.hiv_neg_mother_options())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalarvpreg',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1000M').entry_status, NOT_REQUIRED)
