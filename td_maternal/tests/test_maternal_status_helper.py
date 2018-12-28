from dateutil.relativedelta import relativedelta
from django.utils import timezone
from model_mommy import mommy

from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import (
    POS, YES, NO, NEG, NOT_APPLICABLE, UNK, IND)

from ..maternal_status_helper import MaternalStatusHelper
from .base_test_case import BaseTestCase


class TestMaternalStatusHelper(BaseTestCase):

    def setUp(self):
        super(TestMaternalStatusHelper, self).setUp()

    def test_pos_status_from_enrollment(self):
        """test that we can figure out a positive status
        with just the enrollment status.
        """

        self.create_mother()
        mommy.make_recipe(
            'td_maternal.maternalrando',
            maternal_visit=self.maternal_visit_1010)
        mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.subject_consent.subject_identifier)

        appointement_1020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1020M')
        appointement_2000 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2000M')
        appointement_2010 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2010M')
        appointement_2020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2020M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow() + relativedelta(days=1),
            appointment=appointement_1020)
        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow() + relativedelta(days=2),
            appointment=appointement_2000)
        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow() + relativedelta(days=3),
            appointment=appointement_2010)
        maternal_visit_2020M = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow() + relativedelta(days=4),
            appointment=appointement_2020)

        status_helper = MaternalStatusHelper(maternal_visit_2020M)
        self.assertEqual(status_helper.hiv_status, POS)

    def test_dnapcr_for_heu_infant(self):
        """test that for an HEU infant, then the DNA PCR
        requisition is made available.
        """
        self.create_mother(self.hiv_pos_mother_options())

    def test_ind_status_from_rapid_test(self):
        """test that we can figure out a positive status
        taking in to consideration rapid tests.
        """

        self.create_mother(self.hiv_neg_mother_options())

        maternal_labour_del = mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.subject_consent.subject_identifier)

        appointement_1020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1020M')
        appointement_2000 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2000M')
        appointement_2010 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2010M')
        appointement_2020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2020M')

        appointement_2060 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2060M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_1020)
        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2000)
        maternal_visit_2010M = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=maternal_labour_del.report_datetime,
            appointment=appointement_2010)

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2020)

        status_helper = MaternalStatusHelper(maternal_visit_2010M)

        self.assertEqual(status_helper.hiv_status, NEG)

        mommy.make_recipe(
            'td_maternal.rapidtestresult',
            maternal_visit=maternal_visit_2010M,
            report_datetime=maternal_labour_del.report_datetime,
            result=IND)

        maternal_visit_2060M = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2060)

        status_helper = MaternalStatusHelper(maternal_visit_2060M)
        self.assertEqual(status_helper.hiv_status, IND)

    def test_neg_status_from_enrollment(self):
        """test that we can figure out a negative status with
        just the enrollment status.
        """

        self.create_mother(self.hiv_neg_mother_options())

        maternal_labour_del = mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.subject_consent.subject_identifier)

        appointement_1020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1020M')
        appointement_2000 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2000M')
        appointement_2010 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2010M')
        appointement_2020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2020M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_1020)

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2000)

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=maternal_labour_del.report_datetime,
            appointment=appointement_2010)

        maternal_visit_2020M = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2020)

        status_helper = MaternalStatusHelper(maternal_visit_2020M)
        self.assertEqual(status_helper.hiv_status, NEG)

    def test_neg_status_from_rapid_test(self):
        """test that we can figure out a negative status
        taking in to consideration rapid tests.
        """
        self.create_mother(self.hiv_neg_mother_options())

        maternal_labour_del = mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.subject_consent.subject_identifier)

        appointement_1020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1020M')
        appointement_2000 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2000M')
        appointement_2010 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2010M')

        appointement_2020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2020M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_1020)

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2000)

        maternal_visit_2010M = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=maternal_labour_del.report_datetime,
            appointment=appointement_2010)

        status_helper = MaternalStatusHelper(maternal_visit_2010M)
        self.assertEqual(status_helper.hiv_status, NEG)

        rapid_test = mommy.make_recipe(
            'td_maternal.rapidtestresult',
            maternal_visit=maternal_visit_2010M,
            report_datetime=maternal_visit_2010M.report_datetime,
            result_date=maternal_visit_2010M.report_datetime.date(),
            result=NEG)

        # Visit within 3months of rapid test.
        maternal_visit_2020M = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=rapid_test.report_datetime + relativedelta(months=1),
            appointment=appointement_2020)

        status_helper = MaternalStatusHelper(maternal_visit_2020M)
        self.assertEqual(status_helper.hiv_status, NEG)

    def test_unkown_status(self):
        """test that a negative result that is more than
        3months old will lead to UNK status.
        """
        self.create_mother(self.hiv_neg_mother_options())
        mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.subject_consent.subject_identifier)

        # Appointments
        appointement_1020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1020M')
        appointement_2000 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2000M')
        appointement_2010 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2010M')
        appointement_2020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2020M')

        # Visits
        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_1020)
        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2000)
        maternal_visit_2010M = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2010)

        status_helper = MaternalStatusHelper(maternal_visit_2010M)
        self.assertEqual(status_helper.hiv_status, NEG)

        mommy.make_recipe(
            'td_maternal.rapidtestresult',
            maternal_visit=maternal_visit_2010M,
            result_date=(timezone.now() - relativedelta(months=4)).date(),
            result=NEG)

        # Visit within 3months of rapid test.
        maternal_visit_2020M = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2020)

        status_helper = MaternalStatusHelper(maternal_visit_2020M)
        self.assertEqual(status_helper.hiv_status, UNK)

    def test_return_previous_visit_ordering(self):
        self.create_mother(self.hiv_neg_mother_options())
        mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.subject_consent.subject_identifier)

        appointement_1020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1020M')
        appointement_2000 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2000M')
        appointement_2010 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='2010M')

        # Visits
        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_1020)
        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2000)
        maternal_visit_2010M = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_2010)

        status_helper = MaternalStatusHelper(maternal_visit_2010M)
        self.assertEqual(len(status_helper.previous_visits), 5)

        self.assertEqual(status_helper.previous_visits[0].visit_code, '2010M')
        self.assertEqual(status_helper.previous_visits[4].visit_code, '1000M')

    def test_valid_hiv_neg_week32_test_date(self):
        """Test that NEG status is valid for week32_test_date.
        """

        options = {'current_hiv_status': NEG,
                   'evidence_hiv_status': None,
                   'week32_test': YES,
                   'week32_test_date': (
                       timezone.datetime.now() - relativedelta(weeks=4)).date(),
                   'week32_result': NEG,
                   'evidence_32wk_hiv_status': YES,
                   'will_get_arvs': NOT_APPLICABLE,
                   'rapid_test_done': NO,
                   'rapid_test_date': None,
                   'rapid_test_result': None,
                   'last_period_date': (
                       timezone.datetime.now() - relativedelta(weeks=34)).date()}
        self.antenatal_enrollment = mommy.make_recipe(
            'td_maternal.antenatalenrollment',
            subject_identifier=self.subject_consent.subject_identifier,
            **options)

        self.appointement_1000 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1000M')

        self.maternal_visit_1000 = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=self.appointement_1000)

        self.maternal_ultrasound_initial = mommy.make_recipe(
            'td_maternal.maternalultrasoundinitial',
            report_datetime=self.maternal_visit_1000.report_datetime,
            maternal_visit=self.maternal_visit_1000,
            number_of_gestations=1)

        self.antenatal_visit_membership = mommy.make_recipe(
            'td_maternal.antenatalvisitmembership',
            subject_identifier=self.subject_consent.subject_identifier)

        self.appointement_1020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1010M')

        maternal_visit_1020 = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=self.appointement_1020)

        status_helper = MaternalStatusHelper(maternal_visit_1020)
        self.assertEqual(status_helper.hiv_status, NEG)
