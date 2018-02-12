from django.apps import AppConfig as DjangoApponfig
from django.conf import settings


class AppConfig(DjangoApponfig):
    name = 'td_maternal'
    verbose_name = 'Tshilo Dikotla Maternal CRFs'
    admin_site_name = 'td_maternal_admin'

if settings.APP_NAME == 'td_maternal':

    from datetime import datetime
    from dateutil.tz import gettz
    from edc_appointment.appointment_config import AppointmentConfig
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_constants.constants import FAILED_ELIGIBILITY
    from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
    from edc_visit_tracking.constants import MISSED_VISIT
    from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'td_maternal': ('maternal_visit', 'td_maternal.maternalvisit')}

    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP085'
        protocol_number = '085'
        protocol_name = 'Tshilo Dikotla'
        protocol_title = ''
        study_open_datetime = datetime(
            2016, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2018, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        default_appt_type = 'clinic'
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='td_maternal.maternalvisit')
        ]

    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {'td_maternal.maternalvisit': 'reason'}
        create_on_reasons = [SCHEDULED, UNSCHEDULED]
        delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY, MISSED_VISIT]
