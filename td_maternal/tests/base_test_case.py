from datetime import date

from dateutil.relativedelta import relativedelta
from django.test.testcases import TestCase
from django.utils import timezone
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import (
    YES, NEG, NOT_APPLICABLE, POS, NO)
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy


class BaseTestCase(TestCase):

    def setUp(self):
        self.subject_screening = mommy.make_recipe(
            'td_maternal.subjectscreening')
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        self.subject_consent = mommy.make_recipe(
            'td_maternal.subjectconsent', **options)
        import_holidays()

    def create_mother(self, options=None, report_datetime=None):
        report_datetime = report_datetime or get_utcnow()
        if options:
            self.antenatal_enrollment = mommy.make_recipe(
                'td_maternal.antenatalenrollment',
                subject_identifier=self.subject_consent.subject_identifier,
                **options)
        else:
            self.antenatal_enrollment = mommy.make_recipe(
                'td_maternal.antenatalenrollment',
                subject_identifier=self.subject_consent.subject_identifier,
                report_datetime=report_datetime)

        self.appointement_1000 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1000M')

        self.maternal_visit_1000 = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=report_datetime,
            appointment=self.appointement_1000)

        self.maternal_ultrasound_initial = mommy.make_recipe(
            'td_maternal.maternalultrasoundinitial',
            report_datetime=self.maternal_visit_1000.report_datetime,
            maternal_visit=self.maternal_visit_1000,
            number_of_gestations=1)

        self.antenatal_visit_membership = mommy.make_recipe(
            'td_maternal.antenatalvisitmembership',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=report_datetime)

        self.appointement_1010 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1010M')

        self.maternal_visit_1010 = mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=report_datetime,
            appointment=self.appointement_1010)

    def hiv_pos_mother_options(self):
        options = {'current_hiv_status': POS,
                   'evidence_hiv_status': YES,
                   'will_get_arvs': YES,
                   'is_diabetic': NO,
                   'will_remain_onstudy': YES,
                   'rapid_test_done': NOT_APPLICABLE,
                   'last_period_date': (
                       timezone.datetime.now() - relativedelta(weeks=25)).date()}
        return options

    def hiv_neg_mother_options(self):
        options = {'current_hiv_status': NEG,
                   'evidence_hiv_status': YES,
                   'week32_test': YES,
                   'week32_test_date': (
                       timezone.datetime.now() - relativedelta(weeks=4)).date(),
                   'week32_result': NEG,
                   'evidence_32wk_hiv_status': YES,
                   'will_get_arvs': NOT_APPLICABLE,
                   'rapid_test_done': YES,
                   'rapid_test_date': date.today(),
                   'rapid_test_result': NEG,
                   'last_period_date': (
                       timezone.datetime.now() - relativedelta(weeks=34)).date()}
        return options
