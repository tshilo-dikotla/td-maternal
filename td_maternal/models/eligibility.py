from django.apps import apps
from edc_constants.constants import NO

from ..constants import (MAX_AGE_OF_CONSENT, MIN_AGE_OF_CONSENT)


class Eligibility:

    def __init__(self, age_in_years, has_omang):
        """Returns a tuple (True, None) if mother is eligible otherwise'
        ' (False, error_messsage) where error message is the reason for'
        ' eligibility test failed."""
        self.error_message = []
        self.age_in_years = age_in_years
        self.has_omang = has_omang
        if self.age_in_years < MIN_AGE_OF_CONSENT:
            self.error_message.append(
                'Mother is under {}'.format(MIN_AGE_OF_CONSENT))
        if self.age_in_years > MAX_AGE_OF_CONSENT:
            self.error_message.append(
                'Mother is too old (>{})'.format(MAX_AGE_OF_CONSENT))
        if self.has_omang == NO:
            self.error_message.append('Not a citizen')
        self.is_eligible = False if self.error_message else True

    def __str__(self):
        return "Screened, age ({})".format(self.age_in_years)

    @property
    def maternal_eligibility_loss(self):
        MaternalEligibilityLoss = apps.get_model(
            'td_maternal', 'MaternalEligibilityLoss')
        try:
            maternal_eligibility_loss = MaternalEligibilityLoss.objects.get(
                maternal_eligibility_id=self.id)
        except MaternalEligibilityLoss.DoesNotExist:
            maternal_eligibility_loss = None
        return maternal_eligibility_loss

