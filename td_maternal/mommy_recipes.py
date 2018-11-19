from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, POS
from faker import Faker
from model_mommy.recipe import Recipe, seq

from .models import (
    SubjectConsent, SubjectScreening, AntenatalEnrollment, AntenatalVisitMembership)


fake = Faker()


subjectconsent = Recipe(
    SubjectConsent,
    assessment_score=YES,
    confirm_identity=seq('12315678'),
    consent_copy=YES,
    consent_datetime=get_utcnow(),
    consent_reviewed=YES,
    dob=get_utcnow() - relativedelta(years=25),
    first_name=fake.first_name,
    gender='F',
    identity=seq('12315678'),
    identity_type='country_id',
    initials='XX',
    is_dob_estimated='-',
    is_incarcerated=NO,
    is_literate=YES,
    last_name=fake.last_name,
    screening_identifier=None,
    study_questions=YES,
    site=Site.objects.get_current(),
    subject_identifier=None)

subjectscreening = Recipe(
    SubjectScreening,
    report_datetime=get_utcnow(),
    age_in_years=25,
    has_omang=YES)

antenatalenrollment = Recipe(
    AntenatalEnrollment,
    report_datetime=get_utcnow(),
    current_hiv_status=POS,
    date_at_32wks=(get_utcnow() - relativedelta(months=3)).date(),
    edd_by_lmp=(get_utcnow() - relativedelta(months=4)).date(),
    enrollment_hiv_status=POS,
    evidence_32wk_hiv_status=YES,
    evidence_hiv_status=YES,
    ga_lmp_anc_wks=25,
    ga_lmp_enrollment_wks=24,
    is_diabetic=NO,
    is_eligible=True,
    knows_lmp=YES,
    last_period_date=(get_utcnow() - relativedelta(months=5)).date(),
    pending_ultrasound=False,
    rapid_test_date=None,
    rapid_test_done='N/A',
    rapid_test_result=None,
    week32_result=None,
    week32_test=YES,
    week32_test_date=(get_utcnow() - relativedelta(months=2)).date(),
    will_breastfeed=YES,
    will_get_arvs=YES,
    will_remain_onstudy=YES)


antenatalvisitmembership= Recipe(
    AntenatalVisitMembership,
    antenatal_visits=YES,
    consent_version='3',
    report_datetime=get_utcnow())