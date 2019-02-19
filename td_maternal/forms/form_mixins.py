import arrow
from django import forms
from django.core.exceptions import ValidationError
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from edc_visit_tracking.crf_date_validator import (
    CrfDateValidator, CrfReportDateAllowanceError)

from ..models import MaternalVisit


class SubjectModelFormMixin(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    visit_model = MaternalVisit

    crf_date_validator_cls = CrfDateValidator

    def clean(self):
        try:
            self.crf_date_validator_cls(
                report_datetime=self.cleaned_data.get('report_datetime'),
                visit_report_datetime=self.cleaned_data.get(
                    'maternal_visit').report_datetime,
                created=self.cleaned_data.get('created'),
                modified=self.cleaned_data.get('modified'))
        except CrfReportDateAllowanceError as e:
            raise ValidationError({'report_datetime': e})


class InlineSubjectModelFormMixin(FormValidatorMixin, forms.ModelForm):

    visit_model = MaternalVisit


class PreviousAppointmentFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._previous_appointment_rdate = None
        self._previous_appointment = None

    @property
    def previous_appointment(self):
        if not self._previous_appointment:
            cleaned_data = self.cleaned_data
            self._previous_appointment = cleaned_data.get(
                'maternal_visit').appointment.previous_by_timepoint
        return self._previous_appointment

    @property
    def previous_appointment_rdate(self):
        """Returns the utc arrow object of appt_datetime of the previous
        appointment

        Usage:
            from django.conf import settings
            rdate.to(settings.TIME_ZONE).date()
            rdate.to(settings.TIME_ZONE).datetime
        """
        if not self._previous_appointment_rdate:
            if self.previous_appointment:
                rdate = arrow.Arrow.fromdatetime(
                    self.previous_appointment.appt_datetime,
                    tzinfo=self.previous_appointment.appt_datetime.tzinfo)
            else:
                rdate = None
            self._previous_appointment_rdate = rdate
        return self._previous_appointment_rdate
