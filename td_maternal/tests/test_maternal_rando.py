from django.test import tag
from edc_base.utils import get_utcnow
from model_mommy import mommy

from td_rando.import_randomization_list import import_randomization_list
from td_rando.models.randomization_list import RandomizationList
from td_rando.tests.create_test_list import create_test_list

from .base_test_case import BaseTestCase


@tag('rando')
class TestMaternalRuleGroup(BaseTestCase):

    def setUp(self):
        self.populate_list()
        super(TestMaternalRuleGroup, self).setUp()

    def populate_list(self):
        path = create_test_list(first_sid=1)
        import_randomization_list(path=path, overwrite=True)

    def test_maternal_rando_initial(self):
        self.create_mother(self.hiv_pos_mother_options())
        rando_list = RandomizationList.objects.all().order_by('sid')

        maternalrando = mommy.make_recipe(
            'td_maternal.maternalrando',
            maternal_visit=self.maternal_visit_1010,
            report_datetime=get_utcnow())
        self.assertEqual(maternalrando.sid, rando_list[0].sid)

    def test_maternal_rando_sequential(self):
        self.create_mother(self.hiv_pos_mother_options())
        rando_list = RandomizationList.objects.all().order_by('sid')

        maternalrando = mommy.make_recipe(
            'td_maternal.maternalrando',
            maternal_visit=self.maternal_visit_1010,
            report_datetime=get_utcnow())
        self.assertEqual(maternalrando.sid, rando_list[0].sid)
        self.assertEqual(maternalrando.rx, rando_list[0].drug_assignment)
        self.assertEqual(
            maternalrando.subject_identifier,
            self.subject_consent.subject_identifier)

        self.subject_screening = mommy.make_recipe(
            'td_maternal.subjectscreening')
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        self.subject_consent = mommy.make_recipe(
            'td_maternal.subjectconsent', **options)
        self.create_mother(self.hiv_pos_mother_options())

        maternalrando = mommy.make_recipe(
            'td_maternal.maternalrando',
            maternal_visit=self.maternal_visit_1010,
            report_datetime=get_utcnow())
        self.assertEqual(maternalrando.sid, rando_list[1].sid)
        self.assertEqual(maternalrando.rx, rando_list[1].drug_assignment)
