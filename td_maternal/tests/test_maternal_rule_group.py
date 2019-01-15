from dateutil.relativedelta import relativedelta
from django.test import tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from edc_metadata.constants import REQUIRED, NOT_REQUIRED
from edc_metadata.models import CrfMetadata
from model_mommy import mommy


from .base_test_case import BaseTestCase


class TestMaternalRuleGroup(BaseTestCase):

    def setUp(self):
        super(TestMaternalRuleGroup, self).setUp()

    def test_maternalarvpreg_required(self):
        self.create_mother(self.hiv_pos_mother_options())

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

    def test_maternalsrh_required(self):
        self.create_mother()
        mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow())

        appointment_2000 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2000M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2000)

        appointment_2010 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2010M')
        maternalvisit = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2010)
        mommy.make_recipe(
            'td_maternal.maternalcontraception',
            report_datetime=get_utcnow(),
            maternal_visit=maternalvisit,
            srh_referral=YES)
        appointment_2020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2020M')
        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2020)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalsrh',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='2020M').entry_status, REQUIRED)

    @tag('1')
    def test_maternal_obsterical_history_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        self.assertEqual(
            self.maternal_ultrasound_initial.number_of_gestations, 1)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalobstericalhistory',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1000M').entry_status, REQUIRED)

    def test_maternallifetimearvhistory_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternallifetimearvhistory',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1000M').entry_status, REQUIRED)

    def test_maternallifetimearvhistory_not_required(self):
        self.create_mother(self.hiv_neg_mother_options())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternallifetimearvhistory',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1000M').entry_status, NOT_REQUIRED)

    def test_maternalrando_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalrando',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1010M').entry_status, REQUIRED)

    def test_maternalrando_not_required(self):
        self.create_mother(self.hiv_neg_mother_options())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalrando',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1010M').entry_status, NOT_REQUIRED)

    def test_maternal_interim_idcc_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalrando',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1010M').entry_status, REQUIRED)

    def test_maternal_interim_idcc_not_required(self):
        self.create_mother(self.hiv_neg_mother_options())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalrando',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1010M').entry_status, NOT_REQUIRED)
