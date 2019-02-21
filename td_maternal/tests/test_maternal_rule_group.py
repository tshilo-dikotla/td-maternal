from dateutil.relativedelta import relativedelta
from django.test import tag
from django.utils import timezone
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, NEG
from edc_metadata.constants import REQUIRED, NOT_REQUIRED
from edc_metadata.models import CrfMetadata, RequisitionMetadata
from model_mommy import mommy

from .base_test_case import BaseTestCase


@tag('m_rule')
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

    @tag('1020M')
    def test_maternalarvpreg_required_1020(self):
        self.create_mother(self.hiv_pos_mother_options())

        appointement_1020 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1020M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointement_1020)

        crf = CrfMetadata.objects.filter(
            subject_identifier=self.subject_consent.subject_identifier)

        for x in crf:
            print('>>>>>>>', x.model, x.visit_code)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalarvpreg',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1020M').entry_status, REQUIRED)

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

    @tag('m_rule')
    def test_maternalsrh_not_required(self):
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
            srh_referral=NO)
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
                visit_code='2020M').entry_status, NOT_REQUIRED)

    def test_maternal_obsterical_history_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        self.assertEqual(
            self.maternal_ultrasound_initial.number_of_gestations, 1)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalobstericalhistory',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1000M').entry_status, REQUIRED)

    def test_maternal_obsterical_history_not_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalobstericalhistory',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1000M').entry_status, REQUIRED)

    def test_maternal_medical_history_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalmedicalhistory',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1000M').entry_status, REQUIRED)

    def test_maternal_medical_history_not_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.maternalmedicalhistory',
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

    def test_maternal_post_partum_dep_not_required(self):
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
            'td_maternal.maternalpostpartumdep',
            report_datetime=get_utcnow(),
            maternal_visit=maternalvisit)
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
                model='td_maternal.maternalpostpartumdep',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='2020M').entry_status, NOT_REQUIRED)

    def test_maternal_post_partum_dep_required(self):
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
        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2010)

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
                model='td_maternal.maternalpostpartumdep',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='2020M').entry_status, REQUIRED)

    def test_rapid_test_required_2000M(self):
        self.create_mother(self.hiv_neg_mother_options())
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
        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.rapidtestresult',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='2000M').entry_status, REQUIRED)

    def test_rapid_test_not_required_2000M(self):
        self.create_mother(self.hiv_neg_mother_options())

        mommy.make_recipe(
            'td_maternal.rapidtestresult',
            maternal_visit=self.maternal_visit_1010,
            report_datetime=get_utcnow(),
            result=NEG,
            result_date=get_utcnow().date())

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
        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_maternal.rapidtestresult',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='2000M').entry_status, REQUIRED)

    def test_cd4_panel_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        mommy.make_recipe(
            'td_maternal.maternalinterimidcc',
            maternal_visit=self.maternal_visit_1010,
            report_datetime=get_utcnow(),
            recent_cd4_date=(timezone.datetime.now() - relativedelta(weeks=25)).date())

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='td_maternal.maternalrequisition',
                panel_name='cd4',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1010M').entry_status, REQUIRED)

    def test_cd4_panel_not_required(self):
        self.create_mother(self.hiv_pos_mother_options())

        mommy.make_recipe(
            'td_maternal.maternalinterimidcc',
            maternal_visit=self.maternal_visit_1010,
            report_datetime=get_utcnow(),
            recent_cd4_date=(timezone.datetime.now() - relativedelta(weeks=2)).date())

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='td_maternal.maternalrequisition',
                panel_name='cd4',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1010M').entry_status, NOT_REQUIRED)

    def test_vl_panel_required(self):
        self.create_mother(self.hiv_pos_mother_options())

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

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='td_maternal.maternalrequisition',
                panel_name='viral_load',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='2000M').entry_status, REQUIRED)

    def test_pbmc_vl_required_1010M(self):
        self.create_mother(self.hiv_pos_mother_options())

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='td_maternal.maternalrequisition',
                panel_name='pbmc_vl',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1010M').entry_status, REQUIRED)

    def test_pbmc_pl_required_1010M(self):
        self.create_mother(self.hiv_neg_mother_options())

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='td_maternal.maternalrequisition',
                panel_name='pbmc_pl_store',
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1010M').entry_status, REQUIRED)
