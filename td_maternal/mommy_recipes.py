from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO
from faker import Faker
from model_mommy.recipe import Recipe, seq

from .models import SubjectConsent, SubjectScreening


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
    age_in_years=28,
    has_omang=YES)