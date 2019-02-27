from edc_action_item import site_action_items
from edc_locator.action_items import SubjectLocatorAction


MATERNAL_LOCATOR_ACTION = 'submit-maternal-locator'


class MaternalLocatorAction(SubjectLocatorAction):
    name = MATERNAL_LOCATOR_ACTION
    display_name = 'Submit Maternal Locator'
    reference_model = 'td_maternal.maternallocator'
    admin_site_name = 'td_maternal_admin'


site_action_items.register(MaternalLocatorAction)
