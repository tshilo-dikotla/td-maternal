from datetime import date, datetime
from sys import stdout

from dateutil.relativedelta import relativedelta
from django.db.utils import IntegrityError
from django.test.testcases import TestCase
from django.utils import timezone
from django.utils.timezone import get_current_timezone
from edc_appointment.constants import INCOMPLETE_APPT
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import (
    YES, NEG, NOT_APPLICABLE, POS, NO)
from edc_facility.import_holidays import import_holidays
from edc_registration.exceptions import RegisteredSubjectError
from model_mommy import mommy

from ..models import SubjectConsent


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


def create_mother(self, options=None, options_2=None, omang=None, **kwargs):

    consent_datetime = options_2.get('consent_datetime')
    self.subject_screening = mommy.make_recipe(
        'td_maternal.subjectscreening',
        report_datetime=consent_datetime
    )

    options_ = {
        'screening_identifier': self.subject_screening.screening_identifier,
        'report_datetime': consent_datetime,
        'consent_datetime': consent_datetime,
        'identity': omang,
        'confirm_identity': omang}
    tz = get_current_timezone()
    v2_consent = tz.localize(datetime(2018, 1, 30, 23, 59, 59))
    if consent_datetime < v2_consent:
        version = 1
    else:
        version = 3
    mommy.make_recipe(
        'td_maternal.tdconsentversion',
        screening_identifier=self.subject_screening.screening_identifier,
        report_datetime=consent_datetime,
        version=version)
    options_.update(version=version)
    try:
        self.subject_consent = mommy.make_recipe(
            'td_maternal.subjectconsent', **options_)
    except RegisteredSubjectError as e:
        print(e)
    except IntegrityError:
        pass
    else:
        mommy.make_recipe(
            'td_maternal.specimenconsent',
            subject_identifier=self.subject_consent.subject_identifier,)

        if options:
            if options_2.get('current_hiv_status') == 'Neg':
                options = {
                    'report_datetime': consent_datetime,
                    'current_hiv_status': NEG,
                    'evidence_hiv_status': YES,
                    'week32_test': YES,
                    'week32_test_date': options_2.get('week32_test_date'),
                    'week32_result': NEG,
                    'evidence_32wk_hiv_status': YES,
                    'will_get_arvs': NOT_APPLICABLE,
                    'rapid_test_done': YES,
                    'rapid_test_date': options_2.get('week32_test_date'),
                    'rapid_test_result': NEG,
                    'last_period_date': options_2.get('last_period_date'),
                    'edd_by_lmp': options_2.get('edd_by_lmp')}
                self.antenatal_enrollment = mommy.make_recipe(
                    'td_maternal.antenatalenrollment',
                    subject_identifier=self.subject_consent.subject_identifier,
                    **options)
            else:
                options = {
                    'report_datetime': consent_datetime,
                    'current_hiv_status': POS,
                    'evidence_hiv_status': YES,
                    'will_get_arvs': YES,
                    'is_diabetic': NO,
                    'will_remain_onstudy': YES,
                    'rapid_test_done': NOT_APPLICABLE,
                    'last_period_date': options_2.get('last_period_date'),
                    'edd_by_lmp': options_2.get('edd_by_lmp')}
                self.antenatal_enrollment = mommy.make_recipe(
                    'td_maternal.antenatalenrollment',
                    subject_identifier=self.subject_consent.subject_identifier,
                    **options)
        try:
            self.antenatal_enrollment.save()
            self.appointment_1000 = Appointment.objects.get(
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1000M')
            self.maternal_visit_1000 = mommy.make_recipe(
                'td_maternal.maternalvisit',
                subject_identifier=self.subject_consent.subject_identifier,
                report_datetime=self.appointment_1000.report_datetime,
                appointment=self.appointment_1000)
            self.appointment_1000.appt_status = INCOMPLETE_APPT
            self.appointment_1000.save()
            self.maternal_ultrasound_initial = mommy.make_recipe(
                'td_maternal.maternalultrasoundinitial',
                report_datetime=self.maternal_visit_1000.report_datetime,
                maternal_visit=self.maternal_visit_1000,
                est_edd_ultrasound=options_2.get('est_edd_ultrasound'),
                est_fetal_weight=350,
                number_of_gestations=1)
            self.antenatal_visit_membership = mommy.make_recipe(
                'td_maternal.antenatalvisitmembership',
                report_datetime=consent_datetime,
                subject_identifier=self.subject_consent.subject_identifier)
            self.appointment_1010 = Appointment.objects.get(
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1010M')
            self.maternal_visit_1010 = mommy.make_recipe(
                'td_maternal.maternalvisit',
                subject_identifier=self.subject_consent.subject_identifier,
                report_datetime=self.appointment_1010.report_datetime,
                appointment=self.appointment_1010)
            self.appointment_1010.appt_status = INCOMPLETE_APPT
            self.appointment_1010.save()
            self.appointment_1020 = Appointment.objects.get(
                subject_identifier=self.subject_consent.subject_identifier,
                visit_code='1020M')
            self.maternal_visit_1020 = mommy.make_recipe(
                'td_maternal.maternalvisit',
                subject_identifier=self.subject_consent.subject_identifier,
                report_datetime=self.appointment_1020.report_datetime,
                appointment=self.appointment_1020)
            self.appointment_1020.appt_status = INCOMPLETE_APPT
            self.appointment_1020.save()

            mommy.make_recipe(
                'td_maternal.maternallabourdel',
                subject_identifier=self.subject_consent.subject_identifier,
                delivery_datetime=options_2.get('infant_dob'),
                report_datetime=options_2.get('infant_dob'))
            for x in Appointment.objects.filter(
                    timepoint__gte=30,
                    subject_identifier=self.subject_consent.subject_identifier):
                mommy.make_recipe(
                    'td_maternal.maternalvisit',
                    subject_identifier=self.subject_consent.subject_identifier,
                    report_datetime=x.appt_datetime,
                    appointment=x)
                x.appt_status = INCOMPLETE_APPT
                x.save()
                if x.visit_code == options_2.get('visit_code'):
                    break
            print('Subject Identifier: ', self.subject_consent.subject_identifier,
                  'Visit Code: ', options_2.get('visit_code'))
        except Appointment.DoesNotExist:
            pass
