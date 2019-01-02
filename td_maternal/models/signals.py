from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from edc_identifier.infant_identifier import InfantIdentifier
from edc_registration.models import RegisteredSubject
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .antenatal_enrollment import AntenatalEnrollment
from .antenatal_visit_membership import AntenatalVisitMembership
from .maternal_labour_del import MaternalLabourDel
from .subject_consent import SubjectConsent
from .subject_screening import SubjectScreening
from .maternal_ultrasound_initial import MaternalUltraSoundInitial
from django.core.exceptions import ValidationError


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
        if not created:
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                onschedule_model='td_maternal.onscheduleantenatalenrollment',
                name=instance.schedule_name)
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        else:
            # put subject on schedule
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                onschedule_model='td_maternal.onscheduleantenatalenrollment',
                name=instance.schedule_name)
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
        if not created:
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                'td_maternal.onscheduleantenatalvisitmembership',
                name=instance.schedule_name)
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        else:
            # put subject on schedule
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                'td_maternal.onscheduleantenatalvisitmembership',
                name=instance.schedule_name)
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.report_datetime)


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
            # put subject on schedule
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                'td_maternal.onschedulematernallabourdel',
                name=instance.schedule_name)
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.report_datetime)

        #  Create infant registered subject
        if isinstance(instance, MaternalLabourDel):
            if instance.live_infants_to_register == 1:
                maternal_consent = SubjectConsent.objects.filter(
                    subject_identifier=instance.subject_identifier).order_by('version').last()
                try:
                    maternal_ultrasound = MaternalUltraSoundInitial.objects.filter(
                        maternal_visit__subject_identifier=instance.subject_identifier).order_by('report_datetime').last()
                except MaternalUltraSoundInitial.DoesNotExist:
                    raise ValidationError(
                        f'Maternal Ultrasound Initial must exist for {instance.subject_identifier}')
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
                            RegisteredSubject.objects.get(subject_identifier=infant_identifier.identifier)
                        except RegisteredSubject.DoesNotExist:
                            RegisteredSubject.objects.create(
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
