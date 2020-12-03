from datetime import datetime
import arrow
from dateutil.tz import gettz
from django.apps import apps as django_apps
from edc_constants.constants import FEMALE

from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from .consent_object_validator import ConsentObjectValidator


app_config = django_apps.get_app_config('edc_protocol')
edc_protocol = django_apps.get_app_config('edc_protocol')

tzinfo = gettz('Africa/Gaborone')

v1 = Consent(
    'td_maternal.subjectconsent',
    version='1',
    start=arrow.get(
        datetime(2016, 4, 1, 0, 0, 0), tzinfo=tzinfo).to('UTC').datetime,
    end=arrow.get(
        datetime(2022, 5, 31, 23, 59, 59), tzinfo=tzinfo).to('UTC').datetime,
    age_min=18,
    age_is_adult=18,
    age_max=64,
    gender=[FEMALE])

v3 = Consent(
    'td_maternal.subjectconsent',
    version='3',
    start=arrow.get(
        datetime(2018, 2, 1, 0, 0, 0), tzinfo=tzinfo).to('UTC').datetime,
    end=arrow.get(
        datetime(2022, 5, 31, 23, 59, 59), tzinfo=tzinfo).to('UTC').datetime,
    age_min=18,
    age_is_adult=18,
    age_max=64,
    gender=[FEMALE])

site_consents.validator_cls = ConsentObjectValidator
site_consents.register(v1)
site_consents.register(v3)
