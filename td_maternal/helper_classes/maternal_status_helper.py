from dateutil.relativedelta import relativedelta

from edc_constants.constants import POS, NEG, UNK, IND

from .models import AntenatalEnrollment, RapidTestResult, MaternalInterimIdcc


class MaternalStatusHelper(object):

    def __init__(self, maternal_visit=None):
        self.maternal_visit = maternal_visit

    @property
    def hiv_status(self):
        if not self.maternal_visit:
            return ''
        for visit in self.previous_visits:
            rapid_test_result = None
            try:
                rapid_test_result = RapidTestResult.objects.get(maternal_visit=visit)
            except RapidTestResult.DoesNotExist:
                pass
            else:
                status = self._evaluate_status_from_rapid_tests(
                    (rapid_test_result, 'result', 'result_date'))
                if status in [POS, NEG, UNK, IND]:
                    return status

        # If we have exhausted all visits without a concrete status then use enrollment.
        antenatal_enrollment = AntenatalEnrollment.objects.get(
            subject_identifier=self.maternal_visit.subject_identifier)

        status = self._evaluate_status_from_rapid_tests(
            (antenatal_enrollment, 'enrollment_hiv_status', 'rapid_test_date'))
        if status == UNK:
            # Check that the week32_test_date is still within 3 months
            status = self._evaluate_status_from_rapid_tests(
                (antenatal_enrollment, 'enrollment_hiv_status', 'week32_test_date'))
        if status in [POS, NEG, UNK]:
                return status
        return status

    @property
    def enrollment_hiv_status(self):
        """Return enrollment hiv status.
        """

        try:
            antenatal_enrollment = AntenatalEnrollment.objects.get(
                subject_identifier=self.maternal_visit.subject_identifier)
        except AntenatalEnrollment.DoesNotExist:
            return ''
        else:
            return antenatal_enrollment.enrollment_hiv_status

    @property
    def eligible_for_cd4(self):
        latest_interim_idcc = None
        latest_visit = self.previous_visits.first()
        try:
            latest_interim_idcc = MaternalInterimIdcc.objects.get(
                maternal_visit=latest_visit)
        except MaternalInterimIdcc.DoesNotExist:
            pass
        else:
            three_month_back = latest_visit.report_datetime.date() - relativedelta(months=3)
            if latest_interim_idcc.recent_cd4_date:
                if (three_month_back
                    > latest_interim_idcc.recent_cd4_dat
                        and self.hiv_status == POS):
                    return True
                else:
                    return False
        return True

    @property
    def previous_visits(self):
        return self.maternal_visit.__class__.objects.filter(
            subject_identifier=self.maternal_visit.subject_identifier).order_by(
                '-appointment__timepoint')

    def _evaluate_status_from_rapid_tests(self, instance_result_date_tuple):
        """Return an HIV status.
        """

        if getattr(instance_result_date_tuple[0], instance_result_date_tuple[1]) == POS:
            return POS
        if getattr(instance_result_date_tuple[0], instance_result_date_tuple[1]) == IND:
            return IND
        elif (getattr(instance_result_date_tuple[0], instance_result_date_tuple[1]) == NEG
              and getattr(instance_result_date_tuple[0], instance_result_date_tuple[2])
              and getattr(instance_result_date_tuple[0], instance_result_date_tuple[2])
              > (self.maternal_visit.report_datetime.date() - relativedelta(months=3))):
            return NEG
        else:
            return UNK
