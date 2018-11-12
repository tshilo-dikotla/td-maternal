from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from edc_registration.models import RegisteredSubject
from edc_appointment.models import Appointment
from edc_constants.constants import (
    FEMALE, SCREENED, CONSENTED, FAILED_ELIGIBILITY, ALIVE, OFF_STUDY, ON_STUDY)
from td_maternal.models.subject_consent import SubjectConsent
from .maternal_ultrasound_initial import MaternalUltraSoundInitial
from .antenatal_enrollment import AntenatalEnrollment
from .maternal_eligibility import MaternalEligibility
from .maternal_eligibility_loss import MaternalEligibilityLoss
from .maternal_visit import MaternalVisit
from .maternal_labour_del import MaternalLabourDel


@receiver(post_save, weak=False, dispatch_uid="maternal_eligibility_on_post_save")
def maternal_eligibility_on_post_save(sender, instance, raw, created, using, **kwargs):
    """Creates/Updates RegisteredSubject and creates or deletes MaternalEligibilityLoss
    If participant is consented, does nothing
    * If registered subject does not exist, it will be created and some attrs
      updated from the MaternalEligibility;
    * If registered subject already exists will update some attrs from the MaternalEligibility;
    * If registered subject and consent already exist, does nothing.
    Note: This is the ONLY place RegisteredSubject is created for mothers in this project."""
    if not raw:
        if isinstance(instance, MaternalEligibility) and not kwargs.get('update_fields'):
            if not instance.is_eligible:
                try:
                    maternal_eligibility_loss = MaternalEligibilityLoss.objects.get(
                        maternal_eligibility_id=instance.id)
                    maternal_eligibility_loss.report_datetime = instance.report_datetime
                    maternal_eligibility_loss.reason_ineligible = instance.ineligibility
                    maternal_eligibility_loss.user_modified = instance.user_modified
                    maternal_eligibility_loss.save()
                except MaternalEligibilityLoss.DoesNotExist:
                    MaternalEligibilityLoss.objects.create(
                        maternal_eligibility_id=instance.id,
                        report_datetime=instance.report_datetime,
                        reason_ineligible=instance.ineligibility,
                        user_created=instance.user_created,
                        user_modified=instance.user_modified)
            else:
                MaternalEligibilityLoss.objects.filter(
                    maternal_eligibility_id=instance.id).delete()
                if not instance.is_consented:
                    instance.create_td_consent_version
                try:
                    registered_subject = RegisteredSubject.objects.get(
                        screening_identifier=instance.eligibility_id,
                        subject_type='maternal')
                    SubjectConsent.objects.get(
                        subject_identifier=registered_subject.subject_identifier)
                except RegisteredSubject.DoesNotExist:
                    registered_subject = create_maternal_registered_subject(
                        instance)
                    instance.registered_subject = registered_subject
                    instance.save()
                except SubjectConsent.DoesNotExist:
                    registered_subject = update_maternal_registered_subject(
                        registered_subject, instance)
                    registered_subject.save()


def create_maternal_registered_subject(instance):
    return RegisteredSubject.objects.create(
        created=instance.created,
        first_name='Mother',
        gender=FEMALE,
        registration_status=SCREENED,
        screening_datetime=instance.report_datetime,
        screening_identifier=instance.eligibility_id,
        screening_age_in_years=instance.age_in_years,
        subject_type='maternal',
        user_created=instance.user_created)


def update_maternal_registered_subject(registered_subject, instance):
    registered_subject.first_name = 'Mother'
    registered_subject.gender = FEMALE
    registered_subject.registration_status = SCREENED
    registered_subject.screening_datetime = instance.report_datetime
    registered_subject.screening_identifier = instance.eligibility_id
    registered_subject.screening_age_in_years = instance.age_in_years
    registered_subject.subject_type = 'maternal'
    registered_subject.user_modified = instance.user_modified
    return registered_subject


@receiver(post_save, weak=False, dispatch_uid="maternal_consent_on_post_save")
def maternal_consent_on_post_save(sender, instance, raw, created, using, **kwargs):
    """Update maternal_eligibility consented flag and consent fields on registered subject."""
    if not raw:
        if isinstance(instance, SubjectConsent):
            maternal_eligibility = instance.maternal_eligibility
            if not maternal_eligibility.is_consented:
                maternal_eligibility.is_consented = True
                maternal_eligibility.save(update_fields=['is_consented'])
                maternal_eligibility.registered_subject.registration_datetime = instance.consent_datetime
                maternal_eligibility.registered_subject.registration_status = CONSENTED
                maternal_eligibility.registered_subject.subject_identifier = instance.subject_identifier
                maternal_eligibility.registered_subject.initials = instance.initials
                maternal_eligibility.registered_subject.first_name = instance.first_name
                maternal_eligibility.registered_subject.last_name = instance.last_name
                maternal_eligibility.registered_subject.identity = instance.identity
                maternal_eligibility.registered_subject.dob = instance.dob
                maternal_eligibility.registered_subject.subject_consent_id = instance.id
                maternal_eligibility.registered_subject.subject_consent_id = instance.pk
                maternal_eligibility.registered_subject.save()
            if instance.version == '3':
                try:
                    maternal_labour_del = MaternalLabourDel.objects.get(
                        registered_subject=instance.maternal_eligibility.registered_subject)
                except MaternalLabourDel.DoesNotExist:
                    pass
                else:
                    maternal_labour_del.save()
#                     from td_infant.models import InfantBirth
#                     try:
#                         infant_birth = InfantBirth.objects.get(
#                             maternal_labour_del=maternal_labour_del)
#                     except InfantBirth.DoesNotExist:
#                         pass
#                     else:
#                         infant_birth.save()

#
# @receiver(post_save, weak=False, dispatch_uid="ineligible_take_off_study")
# def ineligible_take_off_study(sender, instance, raw, created, using, **kwargs):
#     """If not is_eligible, creates the 1000M visit and sets to off study."""
#     if not raw:
#         try:
#             if not instance.is_eligible and not instance.pending_ultrasound:
#                 report_datetime = instance.report_datetime
#                 visit_definition = VisitDefinition.objects.get(
#                     code=instance.off_study_visit_code)
#                 appointment = Appointment.objects.get(
#                     registered_subject=instance.registered_subject,
#                     visit_definition=visit_definition)
#                 maternal_visit = MaternalVisit.objects.get(
#                     appointment=appointment)
#                 if maternal_visit.reason != FAILED_ELIGIBILITY:
#                     maternal_visit.reason = FAILED_ELIGIBILITY
#                     maternal_visit.study_status = OFF_STUDY
#                     maternal_visit.save()
#         except MaternalVisit.DoesNotExist:
#             MaternalVisit.objects.create(
#                 appointment=appointment,
#                 report_datetime=report_datetime,
#                 survival_status=ALIVE,
#                 study_status=OFF_STUDY,
#                 reason=FAILED_ELIGIBILITY)
#         except AttributeError as e:
#             pass
#             if 'is_eligible' not in str(e) and 'off_study_visit_code' not in str(e):
#                 raise
#         except VisitDefinition.DoesNotExist:
#             pass
#         except Appointment.DoesNotExist:
#             pass
