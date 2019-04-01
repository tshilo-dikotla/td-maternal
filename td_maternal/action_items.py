from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item import Action, site_action_items, HIGH_PRIORITY
from edc_locator.action_items import SubjectLocatorAction


MATERNAL_LOCATOR_ACTION = 'submit-maternal-locator'
MATERNALOFF_STUDY_ACTION = 'submit-maternaloff-study'
MATERNAL_DEATH_REPORT_ACTION = 'submit-maternal-death-report'
ULTRASOUND_ACTION = 'submit-ultrasound'
MATERNAL_DELIVERY_ACTION = 'submit-maternal-delivery'


class MaternalLocatorAction(SubjectLocatorAction):
    name = MATERNAL_LOCATOR_ACTION
    display_name = 'Submit Maternal Locator'
    reference_model = 'td_maternal.maternallocator'
    admin_site_name = 'td_maternal_admin'


class MaternalUltrasoundAction(Action):
    name = ULTRASOUND_ACTION
    display_name = 'Submit Maternal Ultrasound'
    reference_model = 'td_maternal.maternalultrasoundinitial'
    admin_site_name = 'td_maternal_admin'
    create_by_user = False

    def get_next_actions(self):
        actions = []

        # resave visit to update metadata
        self.reference_model_obj.maternal_visit.save()

        if self.reference_model_obj.number_of_gestations != '1':
            actions = [MaternalOffStudyAction]
        else:
            self.delete_if_new(MaternalOffStudyAction)
        return actions


class MaternalLabourDeliveryAction(Action):
    name = MATERNAL_DELIVERY_ACTION
    display_name = 'Submit Maternal Delivery'
    reference_model = 'td_maternal.maternallabourdel'
    admin_site_name = 'td_maternal_admin'
    priority = HIGH_PRIORITY

    def get_next_actions(self):
        actions = []
        if self.reference_model_obj.live_infants_to_register != 1:
            actions = [MaternalOffStudyAction]
        return actions


class MaternalOffStudyAction(Action):
    name = MATERNALOFF_STUDY_ACTION
    display_name = 'Submit Maternal Offstudy'
    reference_model = 'td_maternal.maternaloffstudy'
    admin_site_name = 'td_maternal_admin'
    priority = HIGH_PRIORITY
    singleton = True


class MaternalDeathReportAction(Action):
    name = MATERNAL_DEATH_REPORT_ACTION
    display_name = 'Submit Maternal Death Report'
    reference_model = 'td_maternal.maternaldeathreport'
    admin_site_name = 'td_maternal_admin'
    priority = HIGH_PRIORITY
    singleton = True

    def get_next_actions(self):
        actions = []
        maternal_deathreport_cls = django_apps.get_model(
            'td_maternal.maternaldeathreport')

        subject_identifier = self.reference_model_obj.subject_identifier
        try:
            maternal_deathreport_cls.objects.get(
                subject_identifier=subject_identifier)
            actions = [MaternalOffStudyAction]
        except ObjectDoesNotExist:
            pass
        return actions


site_action_items.register(MaternalDeathReportAction)
site_action_items.register(MaternalLabourDeliveryAction)
site_action_items.register(MaternalLocatorAction)
site_action_items.register(MaternalOffStudyAction)
site_action_items.register(MaternalUltrasoundAction)
