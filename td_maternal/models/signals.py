from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from edc_constants.constants import YES
from edc_identifier.infant_identifier import InfantIdentifier
from edc_registration.models import RegisteredSubject
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .antenatal_enrollment import AntenatalEnrollment
from .antenatal_visit_membership import AntenatalVisitMembership
from .maternal_labour_del import MaternalLabourDel
from .maternal_ultrasound_initial import MaternalUltraSoundInitial
from .onschedule import OnScheduleAntenatalEnrollment
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

                    schedule.refresh_schedule(
                        subject_identifier=instance.subject_identifier)
                except OnScheduleAntenatalEnrollment.DoesNotExist:

                    schedule.put_on_schedule(
                        subject_identifier=instance.subject_identifier,
                        onschedule_datetime=instance.report_datetime)
        else:
            # put subject on schedule
            if instance.is_eligible:
                schedule.put_on_schedule(
                    subject_identifier=instance.subject_identifier,
                    onschedule_datetime=instance.report_datetime)


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
        if not created:
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                'td_maternal.onschedulematernallabourdel',
                name=instance.schedule_name)
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        else:
            # put subject on schedule if live_infants_to_register is ONLY 1.
            if instance.live_infants_to_register == 1:
                _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                    'td_maternal.onschedulematernallabourdel',
                    name=instance.schedule_name)
                schedule.put_on_schedule(
                    subject_identifier=instance.subject_identifier,
                    onschedule_datetime=instance.report_datetime)

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
