from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, POS, ON_STUDY, ALIVE, PARTICIPANT
from edc_visit_tracking.constants import SCHEDULED
from faker import Faker
from model_mommy.recipe import Recipe, seq
# from td_prn.models import MaternalOffStudy

from .constants import NOT_APPLICABLE
from .models import (
    SubjectConsent, SubjectScreening, AntenatalEnrollment, MaternalSrh,
    AntenatalVisitMembership, MaternalLabourDel, MaternalUltraSoundInitial,
    MaternalVisit, MaternalRando, RapidTestResult, MaternalContraception,
    MaternalPostPartumDep, MaternalInterimIdcc, KaraboSubjectConsent)
from .models import KaraboSubjectScreening
from .models import TdConsentVersion, SpecimenConsent
from .models import MaternalArvPreg, MaternalArv

fake = Faker()

subjectconsent = Recipe(
    SubjectConsent,
    assessment_score=YES,
    identity=seq('12325678', increment_by=1),
    confirm_identity=seq('12325678', increment_by=1),
    consent_copy=YES,
    consent_datetime=get_utcnow(),
    consent_reviewed=YES,
    dob=get_utcnow() - relativedelta(years=25),
    first_name=fake.first_name,
    gender='F',
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

antenatalvisitmembership = Recipe(
    AntenatalVisitMembership,
    antenatal_visits=YES,
    report_datetime=get_utcnow())

maternalvisit = Recipe(
    MaternalVisit,
    report_datetime=get_utcnow(),
    reason=SCHEDULED,
    study_status=ON_STUDY,
    survival_status=ALIVE,
    info_source=PARTICIPANT)

maternalultrasoundinitial = Recipe(
    MaternalUltraSoundInitial,
    report_datetime=get_utcnow(),
    number_of_gestations=1,
    bpd=200,
    hc=200,
    ac=200,
    fl=200,
    ga_by_lmp=100,
    ga_by_ultrasound_wks=7,
    ga_by_ultrasound_days=5,
    est_fetal_weight=700,
    est_edd_ultrasound=get_utcnow().date() + relativedelta(days=90),
    edd_confirmed=get_utcnow() + relativedelta(days=90),
    ga_confirmed=7)

maternallabourdel = Recipe(
    MaternalLabourDel,
    report_datetime=get_utcnow(),
    delivery_datetime=get_utcnow(),
    delivery_time_estimated=NO,
    labour_hrs='3',
    delivery_hospital='Lesirane',
    mode_delivery='spontaneous vaginal',
    csection_reason=NOT_APPLICABLE,
    live_infants_to_register=1,
    valid_regiment_duration=YES)

maternalsrh = Recipe(
    MaternalSrh,
    report_datetime=get_utcnow())

maternalrando = Recipe(
    MaternalRando,
    report_datetime=get_utcnow(),
    randomization_datetime=get_utcnow(),
    dispensed=YES,
    initials='IN',
    delivery_clinic='PMH')

rapidtestresult = Recipe(
    RapidTestResult,
    report_datetime=get_utcnow(),
    rapid_test_done=YES,
    result_date=get_utcnow().date(),
    result=POS)

maternalcontraception = Recipe(
    MaternalContraception,
    more_children=YES,
    contraceptive_partner=NO,
    influential_decision_making='independent_decision',
    uses_contraceptive=YES,
    another_pregnancy=YES,
    pap_smear=YES,
    srh_referral=YES,
)

maternalpostpartumdep = Recipe(
    MaternalPostPartumDep,
    laugh='Not at all',
    enjoyment='As much as I ever did',
    blame='No, never',
    anxious='Yes, very often',
    panick='No, not at all',
    top='No, I have been coping as well as ever',
    unhappy='Yes, some of the time',
    sad='No, never',
    crying='No, never',
    self_harm='Never'
)

maternalinterimidcc = Recipe(
    MaternalInterimIdcc,
    info_since_lastvisit=YES,
    recent_cd4=200.0,
    recent_cd4_date=get_utcnow().date(),
    value_vl_size='equal',
    value_vl=800,
    recent_vl_date=get_utcnow().date(),
)

tdconsentversion = Recipe(
    TdConsentVersion,
    version='3',
    report_datetime=get_utcnow()
)

specimenconsent = Recipe(
    SpecimenConsent,
    consent_datetime=get_utcnow(),
    consent_reviewed=YES,
    assessment_score=YES,
    consent_copy=YES,
    may_store_genetic_samples=YES,
    may_store_samples=YES,
    study_questions=YES,
    consent_signature=YES,
)

karabosubjectconsent = Recipe(
    KaraboSubjectConsent,
    report_datetime=get_utcnow(),
    first_name=fake.first_name,
    last_name=fake.last_name,
    initials='XX',
    language='en',
    is_literate=YES,
    consent_datetime=get_utcnow(),
    identity=seq('212323231', increment_by=1),
    consent_reviewed=YES,
    study_questions=YES,
    assessment_score=YES,
    consent_signature=YES,
    consent_copy=YES,
    site=Site.objects.get_current(),
)

karabosubjectscreening = Recipe(
    KaraboSubjectScreening,
    report_datetime=get_utcnow(),
    infant_alive=YES,
    infant_weight=YES,
    major_anomalies=NO,
    birth_complications=NO,
    infant_documentation=YES,
    infant_months=NO,
    tb_treatment=NO,
    incarcerated=NO,
    willing_to_consent=YES
)

maternalarvpreg = Recipe(
    MaternalArvPreg,
    report_datetime=get_utcnow(),
    took_arv=YES,
    is_interrupt=NO,
    interrupt=None,
)

maternalarvpreg = Recipe(
    MaternalArv,
    report_datetime=get_utcnow(),
    start_date=get_utcnow(),
    stop_date=None,
    arv_code='Any',
)

