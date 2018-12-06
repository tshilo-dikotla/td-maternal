from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .antenatal_enrollment import AntenatalEnrollment
from .antenatal_visit_membership import AntenatalVisitMembership
from .maternal_labour_del import MaternalLabourDel
from .subject_consent import SubjectConsent
from .subject_screening import SubjectScreening


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
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                'td_maternal.onscheduleantenatalvisitmembership')
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        else:
            # put subject on schedule
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                'td_maternal.onscheduleantenatalvisitmembership')
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
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                'td_maternal.onschedulematernallabourdel')
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        else:
            # put subject on schedule
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                'td_maternal.onschedulematernallabourdel')
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.report_datetime)
