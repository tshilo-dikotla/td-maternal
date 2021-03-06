import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = 'td_maternal'
SITE_ID = 40
REVIEWER_SITE_ID = 41
ETC_DIR = os.path.join(BASE_DIR, 'etc')

# RANDOMIZATION_LIST_PATH=os.path.join(BASE_DIR,'test_randomization_list.csv')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jwggbn11gw22h6&0n@q0t97e)&)pg^n_*$18xj350f0%w+ywba'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# AUTO_CREATE_KEYS = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'edc_base.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_fieldsets.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'td_metadata_rules.apps.AppConfig',
    'td_visit_schedule.apps.AppConfig',
    'td_prn.apps.AppConfig',
    'td_labs.apps.AppConfig',
    'td_reference.apps.AppConfig',
    'td_rando.apps.AppConfig',
    'td_infant.apps.AppConfig',
    'td_infant_validators.apps.AppConfig',
    'td_maternal_validators.apps.AppConfig',
    'td_maternal.apps.EdcFacilityAppConfig',
    'td_maternal.apps.EdcVisitTrackingAppConfig',
    'td_maternal.apps.EdcTimepointAppConfig',
    'td_maternal.apps.EdcProtocolAppConfig',
    'td_maternal.apps.EdcAppointmentAppConfig',
    'td_maternal.apps.EdcMetadataAppConfig',
    'td_maternal.apps.EdcLabAppConfig',
    'td_maternal.apps.EdcOdkAppConfig',
    'td_maternal.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'td_maternal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'td_maternal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME':
     'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
     },
    {'NAME':
     'django.contrib.auth.password_validation.MinimumLengthValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.CommonPasswordValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.NumericPasswordValidator',
     },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('af', 'Afrikaans'),
    ('ny', 'Chichewa'),
    ('en', 'English'),
    ('xh', 'isiXhosa'),
    ('lg', 'Luganda'),
    ('rny', 'Runyankore'),
    ('tn', 'Setswana'),
    ('sn', 'Shona'))

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'td_maternal', 'static')
STATIC_URL = '/static/'
DEVICE_ID = '99'

COUNTRY = 'botswana'
HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')
GIT_DIR = BASE_DIR

DEFAULT_STUDY_SITE = '40'

EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USB_VOLUME = None

DASHBOARD_URL_NAMES = {
    'subject_listboard_url': 'td_dashboard:subject_listboard_url',
    'subject_dashboard_url': 'td_dashboard:subject_dashboard_url',
}

if 'test' in sys.argv:

    class DisableMigrations:

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher', )
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
