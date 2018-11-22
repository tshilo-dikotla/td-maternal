from django.test import TestCase
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from django.test.utils import tag


@tag('vs')
class TestVisitSchedule(TestCase):

    def setUp(self):
        pass

    def test_v(self):
        """Test if appointments are created.
        """
        print(site_visit_schedules.visit_schedules, '%%%%%%%%%%%')
