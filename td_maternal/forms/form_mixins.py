import arrow
from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from edc_visit_tracking.crf_date_validator import CrfDateValidator
from edc_visit_tracking.crf_date_validator import CrfReportDateAllowanceError, CrfReportDateBeforeStudyStart
from edc_visit_tracking.crf_date_validator import CrfReportDateIsFuture
from edc_visit_tracking.modelform_mixins import VisitTrackingModelFormMixin
from ..models import MaternalVisit


class SubjectModelFormMixin(SiteModelFormMixin, FormValidatorMixin,
                            forms.ModelForm):

    visit_model = MaternalVisit

    visit_attr = None

    def clean(self):
        visit_codes = ['1000M', '1010M', '1020M']
        cleaned_data = super().clean()
        if (cleaned_data.get('maternal_visit')
                and cleaned_data.get('maternal_visit').visit_code
                not in visit_codes):
            if cleaned_data.get('report_datetime'):
                try:
                    CrfDateValidator(
                        report_datetime=cleaned_data.get('report_datetime'),
                        visit_report_datetime=cleaned_data.get(
                            self._meta.model.visit_model_attr()).report_datetime)
                except (CrfReportDateAllowanceError, CrfReportDateBeforeStudyStart,
                        CrfReportDateIsFuture) as e:
                    raise forms.ValidationError(e)
        return cleaned_data


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
