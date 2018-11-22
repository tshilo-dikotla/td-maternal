from edc_visit_schedule import site_visit_schedules
from django.test import TestCase, tag


@tag('1')
class TestVisitSchedule(TestCase):

    def setUp(self):
        TestCase.setUp(self)

    def test_visit_schedules(self):
        print(site_visit_schedules.visit_schedules,
              "***********")
