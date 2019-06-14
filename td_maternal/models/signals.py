from django.apps import apps as django_apps
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import transaction
from django.db.models.deletion import ProtectedError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from edc_constants.constants import YES
from edc_identifier.infant_identifier import InfantIdentifier
from edc_registration.models import RegisteredSubject

from edc_appointment.constants import COMPLETE_APPT, IN_PROGRESS_APPT, INCOMPLETE_APPT
from edc_appointment.models import Appointment
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .antenatal_enrollment import AntenatalEnrollment
from .antenatal_visit_membership import AntenatalVisitMembership
from .maternal_labour_del import MaternalLabourDel
from .maternal_ultrasound_initial import MaternalUltraSoundInitial
from .onschedule import OnScheduleAntenatalEnrollment, OnScheduleMaternalLabourDel
from .onschedule import OnScheduleAntenatalVisitMembership
from .subject_consent import SubjectConsent
from .subject_screening import SubjectScreening


INFANT = 'infant'


@receiver(post_save, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """Update subject screening consented flag.
    """
    if not raw:
        if created:
            subject_screening = SubjectScreening.objects.get(
                screening_identifier=instance.screening_identifier)
            subject_screening.subject_identifier = instance.subject_identifier
            subject_screening.is_consented = True
            subject_screening.save_base(
                update_fields=['subject_identifier', 'is_consented'])
            if instance.version == '3':
                try:
                    SubjectConsent.objects.get(
                        subject_identifier=instance.subject_identifier,
                        version='1')
                except SubjectConsent.DoesNotExist:
                    pass
                else:
                    take_off_schedule(
                        subject_identifier=instance.subject_identifier, version=instance.version)


@receiver(post_save, weak=False, sender=AntenatalEnrollment,
          dispatch_uid='antenatal_enrollment_on_post_save')
def antenatal_enrollment_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an onschedule instance for this antenatal enrollment, if
    it does not exist.
    """
    if not raw:
        _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
            onschedule_model='td_maternal.onscheduleantenatalenrollment',
            name=instance.schedule_name)
        if not created:
            if instance.is_eligible:
                try:
                    OnScheduleAntenatalEnrollment.objects.get(
                        subject_identifier=instance.subject_identifier)
                except OnScheduleAntenatalEnrollment.DoesNotExist:
                    schedule.put_on_schedule(
                        subject_identifier=instance.subject_identifier,
                        onschedule_datetime=instance.report_datetime)
                    add_schedule_name(model_obj=OnScheduleAntenatalEnrollment,
                                      subject_identifier=instance.subject_identifier,
                                      schedule_name=instance.schedule_name)
                else:
                    schedule.refresh_schedule(
                        subject_identifier=instance.subject_identifier)
        else:
            # put subject on schedule
            if instance.is_eligible:
                schedule.put_on_schedule(
                    subject_identifier=instance.subject_identifier,
                    onschedule_datetime=instance.report_datetime)
                add_schedule_name(model_obj=OnScheduleAntenatalEnrollment,
                                  subject_identifier=instance.subject_identifier,
                                  schedule_name=instance.schedule_name)


@receiver(post_save, weak=False, sender=AntenatalVisitMembership,
          dispatch_uid='antenatal_visit_membership_on_post_save')
def antenatal_visit_membership_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an onschedule instance for this antenatal visit membership, if
    it does not exist.
    """
    if not raw:
        antenatal_enroll_model = django_apps.get_model(
            'td_maternal.onscheduleantenatalvisitmembership')
        if not created or instance.antenatal_visits == YES:
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                'td_maternal.onscheduleantenatalvisitmembership',
                name=instance.schedule_name)
            try:
                antenatal_enroll_model.objects.get(
                    subject_identifier=instance.subject_identifier)
            except antenatal_enroll_model.DoesNotExist:
                if instance.antenatal_visits == YES:
                    schedule.put_on_schedule(
                        subject_identifier=instance.subject_identifier,
                        onschedule_datetime=instance.report_datetime)

                    add_schedule_name(model_obj=OnScheduleAntenatalVisitMembership,
                                      subject_identifier=instance.subject_identifier,
                                      schedule_name=instance.schedule_name)
            else:
                schedule.refresh_schedule(
                    subject_identifier=instance.subject_identifier)


@receiver(post_save, weak=False, sender=MaternalLabourDel,
          dispatch_uid='maternal_labour_del_on_post_save')
def maternal_labour_del_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an onschedule instance for this maternal labour delivery, if
    it does not exist.
    """
    if not raw:
        _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
            'td_maternal.onschedulematernallabourdel',
            name=instance.schedule_name)
        try:

            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        except ObjectDoesNotExist:
            # put subject on schedule if live_infants_to_register is ONLY 1.
            if instance.live_infants_to_register == 1:
                schedule.put_on_schedule(
                    subject_identifier=instance.subject_identifier,
                    onschedule_datetime=instance.report_datetime)
                add_schedule_name(model_obj=OnScheduleMaternalLabourDel,
                                  subject_identifier=instance.subject_identifier,
                                  schedule_name=instance.schedule_name)
                create_registered_infant(instance)


def create_registered_infant(instance):

    #  Create infant registered subject
    if isinstance(instance, MaternalLabourDel):
        if instance.live_infants_to_register == 1:
            maternal_consent = SubjectConsent.objects.filter(
                subject_identifier=instance.subject_identifier
            ).order_by('version').last()
            try:
                maternal_ultrasound = MaternalUltraSoundInitial.objects.filter(
                    maternal_visit__subject_identifier=instance.subject_identifier
                ).order_by('report_datetime').last()
            except MaternalUltraSoundInitial.DoesNotExist:
                raise ValidationError(
                    'Maternal Ultrasound Initial must exist for'
                    f' {instance.subject_identifier}')
            else:
                with transaction.atomic():
                    infant_identifier = InfantIdentifier(
                        maternal_identifier=instance.subject_identifier,
                        birth_order=1,
                        live_infants=int(
                            maternal_ultrasound.number_of_gestations),
                        registration_status='DELIVERED',
                        registration_datetime=instance.delivery_datetime,
                        subject_type=INFANT)
                    try:
                        registered_subject = RegisteredSubject.objects.get(
                            subject_identifier=infant_identifier.identifier)
                    except RegisteredSubject.DoesNotExist:
                        registered_subject = RegisteredSubject.objects.create(
                            subject_identifier=infant_identifier.identifier,
                            registration_datetime=instance.delivery_datetime,
                            subject_type=INFANT,
                            user_created=instance.user_created,
                            created=timezone.now(),
                            first_name='No Name',
                            initials=None,
                            registration_status='DELIVERED',
                            relative_identifier=maternal_consent.subject_identifier,
                            site=maternal_consent.site)
                    # Create infant dummy consent
                    infant_consent_model_cls = django_apps.get_model(
                        'td_infant.infantdummysubjectconsent')
                    try:
                        infant_consent_model_cls.objects.get(
                            subject_identifier=registered_subject.subject_identifier)
                    except infant_consent_model_cls.DoesNotExist:
                        infant_consent_model_cls.objects.create(
                            subject_identifier=registered_subject.subject_identifier,
                            version=maternal_consent.version,
                            report_datetime=instance.report_datetime,
                            consent_datetime=timezone.now())


def add_schedule_name(model_obj=None, subject_identifier=None, schedule_name=None):
    try:
        onschedule_antenatal = model_obj.objects.get(
            subject_identifier=subject_identifier,
            schedule_name__isnull=True)
    except model_obj.DoesNotExist:
        pass
    else:
        onschedule_antenatal.schedule_name = schedule_name
        onschedule_antenatal.save()


def take_off_schedule(subject_identifier=None, version=None):
    '''This method is meant to move participant from one schedule i.e
    any v1 schedule to v3 when a participant reconsents.

    This is not to be confused with Off study. Off study removes
    participants completely from ALL schedules.
    '''
    infant_appointment = django_apps.get_model(
        'td_infant.appointment')

    infant_birth_onschedule = django_apps.get_model(
        'td_infant.onscheduleinfantbirth')
    maternal_labour_del_schedule = django_apps.get_model(
        'td_maternal.onschedulematernallabourdel')
    antenatal_visit_membership_schedule = django_apps.get_model(
        'td_maternal.onscheduleantenatalvisitmembership')
    antenatal_enrollment_schedule = django_apps.get_model(
        'td_maternal.onscheduleantenatalenrollment')
    maternal_schedules = [maternal_labour_del_schedule,
                          antenatal_visit_membership_schedule,
                          antenatal_enrollment_schedule]
    for on_schedule in maternal_schedules:
        try:
            on_schedule_obj = on_schedule.objects.get(
                subject_identifier=subject_identifier)
        except on_schedule.DoesNotExist:
            pass
        else:
            # get old schedule and put participant offschedule
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                onschedule_model=on_schedule._meta.label_lower,
                name=on_schedule_obj.schedule_name)
            schedule.take_off_schedule(subject_identifier=subject_identifier)

            # put participant on new version schedule
            v3_schedule_name = schedule.name[:-1] + version
            _, v3_schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                onschedule_model=on_schedule._meta.label_lower,
                name=v3_schedule_name)
            v3_schedule.put_on_schedule(
                subject_identifier=subject_identifier,
                onschedule_datetime=on_schedule_obj.report_datetime,
                schedule_name=v3_schedule_name)
            add_schedule_name(model_obj=on_schedule,
                              subject_identifier=subject_identifier,
                              schedule_name=v3_schedule_name)

            # remove mothers appointments that already exist on the old schedule from
            # the new one
            delete_appointments_new_schedule(
                appointment_obj=Appointment,
                old_schedule=schedule.name,
                new_schedule=v3_schedule_name,
                subject_identifier=subject_identifier)

            if check_labour_del(subject_identifier=subject_identifier):
                # get old infant schedule and put participant offschedule
                # TODO: get infant schedule names without hardcoding
                infant_subject_identifier = subject_identifier + '-10'
                _, infant_schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                    onschedule_model=infant_birth_onschedule._meta.label_lower,
                    name='infant_schedule_v1')
                infant_schedule.take_off_schedule(
                    subject_identifier=infant_subject_identifier)

                infant_v3_schedule_name = infant_schedule.name[:-1] + version
                _, infant_v3_schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                    onschedule_model=infant_birth_onschedule._meta.label_lower,
                    name=infant_v3_schedule_name)

                infant_v3_schedule.put_on_schedule(
                    subject_identifier=infant_subject_identifier,
                    onschedule_datetime=on_schedule_obj.report_datetime,
                    schedule_name=infant_v3_schedule_name)
                add_schedule_name(model_obj=on_schedule,
                                  subject_identifier=infant_subject_identifier,
                                  schedule_name=infant_v3_schedule_name)
                # update infant schedules
                delete_appointments_new_schedule(
                    appointment_obj=infant_appointment,
                    old_schedule='infant_schedule_v1',
                    new_schedule=infant_v3_schedule.name,
                    subject_identifier=infant_subject_identifier)
            break


def check_labour_del(subject_identifier):
    try:
        return MaternalLabourDel.objects.get(
            subject_identifier=subject_identifier,
            live_infants_to_register=1)
    except MaternalLabourDel.DoesNotExist:
        return None


def delete_appointments_new_schedule(
        appointment_obj=None, old_schedule=None,
        new_schedule=None, subject_identifier=None):

    appointment_old = appointment_obj.objects.filter(
        schedule_name=old_schedule,
        subject_identifier=subject_identifier,
        appt_status__in=[COMPLETE_APPT, IN_PROGRESS_APPT, INCOMPLETE_APPT]).order_by('timepoint').last()

    if appointment_old:
        appointments_new = appointment_obj.objects.filter(
            schedule_name=new_schedule,
            subject_identifier=subject_identifier,
            timepoint__lte=appointment_old.timepoint)

        for appointment in appointments_new:
            try:
                appointment.delete()
            except ProtectedError:
                pass
