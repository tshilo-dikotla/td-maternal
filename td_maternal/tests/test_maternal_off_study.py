from dateutil.relativedelta import relativedelta
from django.test import tag
from django.utils import timezone
from edc_base.utils import get_utcnow
from edc_visit_tracking.crf_date_validator import CrfReportDateAllowanceError
from model_mommy import mommy

from .base_test_case import BaseTestCase


@tag('offstudy')
class TestTDOffStudy(BaseTestCase):

    def setUp(self):
        super(TestTDOffStudy, self).setUp()
        self.create_mother(self.hiv_pos_mother_options())

    def test_subject_put_offstudy(self):
        mommy.make_recipe(
            'td_maternal.maternaloffstudy',
            subject_identifier=self.subject_consent.subject_identifier,
            offstudy_date=get_utcnow().date(),
            report_datetime=get_utcnow(),
            reason='multiple_vialble_gestations')

        self.assertRaises(
            CrfReportDateAllowanceError,
            mommy.make_recipe, 'td_maternal.maternalinterimidcc',
            maternal_visit=self.maternal_visit_1010,
            report_datetime=timezone.datetime.now() - relativedelta(days=4)
        )
