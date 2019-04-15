from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO
from edc_constants.constants import NO, YES
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_protocol.validators import date_not_before_study_start

from ..models.subject_consent import SubjectConsent
from .enrollment_mixin import EnrollmentMixin


class AntenatalEnrollment(UniqueSubjectIdentifierFieldMixin,
                          EnrollmentMixin, BaseUuidModel):

    knows_lmp = models.CharField(
        verbose_name="Does the mother know the approximate date "
        "of the first day her last menstrual period?",
        choices=YES_NO,
        help_text='LMP',
        max_length=3)

    last_period_date = models.DateField(
        verbose_name="What is the approximate date of the first day of "
        "the mother’s last menstrual period",
        validators=[
            date_not_before_study_start,
            date_not_future, ],
        null=True,
        blank=True,
        help_text='LMP')

    ga_lmp_enrollment_wks = models.IntegerField(
        verbose_name="GA by LMP at enrollment.",
        help_text=" (weeks of gestation at enrollment, LMP). Eligible if"
        " >16 and <36 weeks GA",
        null=True,
        blank=True,)

    ga_lmp_anc_wks = models.IntegerField(
        verbose_name="What is the mother's gestational age according to"
        " ANC records?",
        validators=[MinValueValidator(1), MaxValueValidator(40)],
        null=True,
        blank=True,
        help_text=" (weeks of gestation at enrollment, ANC)",)

    edd_by_lmp = models.DateField(
        verbose_name="Estimated date of delivery by lmp",
        validators=[
            date_not_before_study_start],
        null=True,
        blank=True,
        help_text="")

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.consent_version = self.get_consent_version()
        super(AntenatalEnrollment, self).save(*args, **kwargs)

    def __str__(self):
        return f'antenatal: {self.subject_identifier}'

#     def natural_key(self):
#         return self.registered_subject.natural_key()
#     natural_key.dependencies = ['edc_registration.registeredsubject']

    def unenrolled_error_messages(self):
        """Returns a tuple (True, None) if mother is eligible otherwise
        (False, unenrolled_error_message) where error message is the reason
        enrollment failed."""

        unenrolled_error_message = []
        chronic_message = self.chronic_unenrolled_error_messages()
        unenrolled_error_message.append(
            chronic_message) if chronic_message else None
        if self.will_breastfeed == NO:
            unenrolled_error_message.append('will not breastfeed')
        if self.will_remain_onstudy == NO:
            unenrolled_error_message.append('won\'t remain in study')
        if self.will_get_arvs == NO:
            unenrolled_error_message.append(
                'Will not get ARVs on this pregnancy.')
        if self.rapid_test_done == NO:
            unenrolled_error_message.append('rapid test not done')
        if (self.ga_lmp_enrollment_wks and
                (self.ga_lmp_enrollment_wks < 16 or
                 self.ga_lmp_enrollment_wks > 36)):
            unenrolled_error_message.append('gestation not 16 to 36wks')
        if self.delivery and not self.delivery.keep_on_study:
            unenrolled_error_message.append(
                'Hiv+ and not on ART for atleast 4 weeks.')
        if self.ultrasound and not self.ultrasound.pass_antenatal_enrollment:
            unenrolled_error_message.append('Pregnancy is not a singleton.')
        return unenrolled_error_message

    def chronic_unenrolled_error_messages(self):
        unenrolled_error_message = None
        if self.is_diabetic == YES:
            unenrolled_error_message = 'Diabetic'
        return unenrolled_error_message

    def get_consent_version(self):
        subject_screening_cls = django_apps.get_model(
            'td_maternal.subjectscreening')
        consent_version_cls = django_apps.get_model(
            'td_maternal.tdconsentversion')
        try:
            subject_screening_obj = subject_screening_cls.objects.get(
                subject_identifier=self.subject_identifier)
        except subject_screening_cls.DoesNotExist:
            raise ValidationError(
                'Missing Subject Screening form. Please complete '
                'it before proceeding.')
        else:
            try:
                consent_version_obj = consent_version_cls.objects.get(
                    screening_identifier=subject_screening_obj.screening_identifier)
            except consent_version_cls.DoesNotExist:
                raise ValidationError(
                    'Missing Consent Version form. Please complete '
                    'it before proceeding.')
            return consent_version_obj.version

    @property
    def schedule_name(self):
        """Return a visit schedule name.
        """
        schedule_name = None
        subject_consent = SubjectConsent.objects.filter(
            subject_identifier=self.subject_identifier).order_by('version').last()
        if subject_consent.version == '1':
            schedule_name = 'antenatal_schedule_1'
        elif subject_consent.version == '3':
            schedule_name = 'antenatal_schedule_3'
        return schedule_name

    @property
    def off_study_visit_code(self):
        """Returns the visit code for the off-study visit if eligibility
        criteria fail."""
        return '1000M'

    class Meta:
        app_label = 'td_maternal'
        verbose_name = 'Antenatal Enrollment'
        verbose_name_plural = 'Antenatal Enrollment'
