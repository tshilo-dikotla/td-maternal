from django.test import TestCase, tag
from edc_base.utils import get_utcnow


class MaternalArvPregForm(TestCase):

    def setUp(self):
        self.data = {
            'maternalarv_set-0-start_date': get_utcnow(),
            'maternalarv_set-0-arv_code': 'AZT',
            'maternalarv_set-0-stop_date': None,
            'maternalarv_set-1-start_date': get_utcnow(),
            'maternalarv_set-1-stop_date': None,
            'maternalarv_set-1-arv_code': '3TC',
            'maternalarv_set-2-start_date': get_utcnow(),
            'maternalarv_set-2-stop_date': 'MLS',
            'maternalarv_set-2-arv_code': None,
        }

    def test_match_prev_arvs(self):
        pass
