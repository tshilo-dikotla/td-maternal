from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy

from edc_appointment.constants import INCOMPLETE_APPT
from edc_appointment.models import Appointment
from td_infant.models import Appointment as InfantAppointment

from ..models import OnScheduleAntenatalVisitMembership, OnScheduleMaternalLabourDel
from ..models import SubjectConsent, MaternalOffSchedule, OnScheduleAntenatalEnrollment


@tag('recon')
class TestSubjectConsent(TestCase):

    def setUp(self):
        import_holidays()

        self.subject_screening = mommy.make_recipe(
            'td_maternal.subjectscreening')

        self.td_consent_version = mommy.make_recipe(
            'td_maternal.tdconsentversion',
            screening_identifier=self.subject_screening.screening_identifier,
            version='1')

        self.options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow,
            'first_name': 'TESTING',
            'last_name': 'TESTING',
            'initials': 'TT',
            'identity': '122222222',
            'confirm_identity': '122222222',
            'version': '1'}
        self.consent_v1 = mommy.make_recipe(
            'td_maternal.subjectconsent', **self.options)

        mommy.make_recipe(
            'td_maternal.antenatalenrollment',
            subject_identifier=self.consent_v1.subject_identifier,
            report_datetime=get_utcnow)

    def test_reconsent_participant_1000M(self):

        self.td_consent_version.version = '3'
        self.td_consent_version.save()

        self.options.update(version='3')
        mommy.make_recipe(
            'td_maternal.subjectconsent',
            subject_identifier=self.consent_v1.subject_identifier,
            **self.options)
        self.assertEqual(SubjectConsent.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 2)

        self.assertEqual(MaternalOffSchedule.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier,).count(), 1)
        self.assertEqual(Appointment.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 2)

        self.assertEqual(OnScheduleAntenatalEnrollment.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 2)

    def test_reconsent_participant_visit_membership(self):

        appointment_1000 = Appointment.objects.get(
            subject_identifier=self.consent_v1.subject_identifier,
            visit_code='1000M')

        maternal_visit_1000 = mommy.make_recipe(
            'td_maternal.maternalvisit',
            report_datetime=get_utcnow(),
            subject_identifier=self.consent_v1.subject_identifier,
            appointment=appointment_1000)

        mommy.make_recipe(
            'td_maternal.maternalultrasoundinitial',
            report_datetime=maternal_visit_1000.report_datetime,
            maternal_visit=maternal_visit_1000,
            number_of_gestations=1)

        appointment_1000.appt_status = INCOMPLETE_APPT
        appointment_1000.save()

        mommy.make_recipe(
            'td_maternal.antenatalvisitmembership',
            subject_identifier=self.consent_v1.subject_identifier)

        appointment_1010 = Appointment.objects.get(
            subject_identifier=self.consent_v1.subject_identifier,
            visit_code='1010M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.consent_v1.subject_identifier,
            appointment=appointment_1010)

        appointment_1010.appt_status = INCOMPLETE_APPT
        appointment_1010.save()

        self.assertEqual(Appointment.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 3)

        self.td_consent_version.version = '3'
        self.td_consent_version.save()

        self.options.update(version='3')
        mommy.make_recipe(
            'td_maternal.subjectconsent',
            subject_identifier=self.consent_v1.subject_identifier,
            **self.options)
        self.assertEqual(SubjectConsent.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 2)

        self.assertEqual(MaternalOffSchedule.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier,).count(), 1)

        self.assertEqual(Appointment.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 3)

        self.assertEqual(OnScheduleAntenatalVisitMembership.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 2)

    def test_reconsent_participant_post_delivery(self):

        appointment_1000 = Appointment.objects.get(
            subject_identifier=self.consent_v1.subject_identifier,
            visit_code='1000M')

        maternal_visit_1000 = mommy.make_recipe(
            'td_maternal.maternalvisit',
            report_datetime=get_utcnow(),
            subject_identifier=self.consent_v1.subject_identifier,
            appointment=appointment_1000)

        mommy.make_recipe(
            'td_maternal.maternalultrasoundinitial',
            report_datetime=maternal_visit_1000.report_datetime,
            maternal_visit=maternal_visit_1000,
            number_of_gestations=1)

        appointment_1000.appt_status = INCOMPLETE_APPT
        appointment_1000.save()

        mommy.make_recipe(
            'td_maternal.antenatalvisitmembership',
            subject_identifier=self.consent_v1.subject_identifier)

        appointment_1010 = Appointment.objects.get(
            subject_identifier=self.consent_v1.subject_identifier,
            visit_code='1010M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.consent_v1.subject_identifier,
            appointment=appointment_1010)

        appointment_1010.appt_status = INCOMPLETE_APPT
        appointment_1010.save()

        appointment_1020 = Appointment.objects.get(
            subject_identifier=self.consent_v1.subject_identifier,
            visit_code='1020M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            report_datetime=get_utcnow(),
            subject_identifier=self.consent_v1.subject_identifier,
            appointment=appointment_1020)

        appointment_1020.appt_status = INCOMPLETE_APPT
        appointment_1020.save()

        mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.consent_v1.subject_identifier)

        mommy.make_recipe(
            'td_infant.infantbirth',
            subject_identifier=self.consent_v1.subject_identifier + '-10',
            report_datetime=get_utcnow())

        for appointment in Appointment.objects.filter(
                subject_identifier=self.consent_v1.subject_identifier,
                schedule_name='mld_schedule_1').order_by('timepoint'):

            mommy.make_recipe(
                'td_maternal.maternalvisit',
                report_datetime=get_utcnow(),
                subject_identifier=self.consent_v1.subject_identifier,
                appointment=appointment)
            appointment.appt_status = INCOMPLETE_APPT
            appointment.save()
            if appointment.visit_code == '2060M':
                break

        self.td_consent_version.version = '3'
        self.td_consent_version.save()

        self.options.update(version='3')
        mommy.make_recipe(
            'td_maternal.subjectconsent',
            subject_identifier=self.consent_v1.subject_identifier,
            **self.options)

        self.assertEqual(SubjectConsent.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 2)

        self.assertEqual(MaternalOffSchedule.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier,).count(), 1)

        self.assertEqual(Appointment.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 12)

        self.assertEqual(OnScheduleMaternalLabourDel.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 2)

    def test_reconsent_participant_infant(self):

        appointment_1000 = Appointment.objects.get(
            subject_identifier=self.consent_v1.subject_identifier,
            visit_code='1000M')

        maternal_visit_1000 = mommy.make_recipe(
            'td_maternal.maternalvisit',
            report_datetime=get_utcnow(),
            subject_identifier=self.consent_v1.subject_identifier,
            appointment=appointment_1000)

        mommy.make_recipe(
            'td_maternal.maternalultrasoundinitial',
            report_datetime=maternal_visit_1000.report_datetime,
            maternal_visit=maternal_visit_1000,
            number_of_gestations=1)

        appointment_1000.appt_status = INCOMPLETE_APPT
        appointment_1000.save()

        mommy.make_recipe(
            'td_maternal.antenatalvisitmembership',
            subject_identifier=self.consent_v1.subject_identifier)

        appointment_1010 = Appointment.objects.get(
            subject_identifier=self.consent_v1.subject_identifier,
            visit_code='1010M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.consent_v1.subject_identifier,
            appointment=appointment_1010)

        appointment_1010.appt_status = INCOMPLETE_APPT
        appointment_1010.save()

        appointment_1020 = Appointment.objects.get(
            subject_identifier=self.consent_v1.subject_identifier,
            visit_code='1020M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            report_datetime=get_utcnow(),
            subject_identifier=self.consent_v1.subject_identifier,
            appointment=appointment_1020)

        appointment_1020.appt_status = INCOMPLETE_APPT
        appointment_1020.save()

        mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.consent_v1.subject_identifier)

        mommy.make_recipe(
            'td_infant.infantbirth',
            subject_identifier=self.consent_v1.subject_identifier + '-10',
            report_datetime=get_utcnow())

        for appointment in InfantAppointment.objects.filter(
                subject_identifier=self.consent_v1.subject_identifier + '-10',
                schedule_name='infant_schedule_v1').order_by('timepoint'):

            mommy.make_recipe(
                'td_infant.infantvisit',
                report_datetime=get_utcnow(),
                subject_identifier=self.consent_v1.subject_identifier + '-10',
                appointment=appointment)
            appointment.appt_status = INCOMPLETE_APPT
            appointment.save()
            if appointment.visit_code == '2060':
                break

        self.td_consent_version.version = '3'
        self.td_consent_version.save()

        self.options.update(version='3')
        mommy.make_recipe(
            'td_maternal.subjectconsent',
            subject_identifier=self.consent_v1.subject_identifier,
            **self.options)

        self.assertEqual(SubjectConsent.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 2)

        self.assertEqual(MaternalOffSchedule.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier,).count(), 1)

        self.assertEqual(InfantAppointment.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier + '-10').count(), 9)

        self.assertEqual(OnScheduleMaternalLabourDel.objects.filter(
            subject_identifier=self.consent_v1.subject_identifier).count(), 2)
