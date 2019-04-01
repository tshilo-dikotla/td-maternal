from edc_constants.constants import YES, NO


class KaraboEligibility:

    def __init__(self, infant_alive=None, infant_weight=None,
                 major_anomalies=None, birth_complications=None,
                 infant_documentation=None, infant_months=None,
                 tb_treatment=None, incarcerated=None,
                 willing_to_consent=None):

        self.eligible = True
        self.reasons_ineligible = []

        if infant_alive == NO:
            self.eligible = False
            self.reasons_ineligible = 'Infant is not alive'

        if infant_weight == NO:
            self.eligible = False
            self.reasons_ineligible = 'Infant weight < 2.00 kilograms'

        if major_anomalies == YES:
            self.eligible = False
            self.reasons_ineligible = 'Infant was born with major'
            ' congenital anomalies'

        if birth_complications == YES:
            self.eligible = False
            self.reasons_ineligible = 'Infant experienced birth complications'

        if infant_documentation == NO:
            self.eligible = False
            self.reasons_ineligible = 'Infant does not have documentation that'
            ' they received a BCG vaccine within 72 hours of birth'
            ' in the Under 5 Health '

        if infant_months == YES:
            self.eligible = False
            self.reasons_ineligible = 'Infant has reached 14 months of age '

        if tb_treatment == NO:
            self.eligible = False
            self.reasons_ineligible = 'Woman was not being in tb treatment'
            ' during pregnancy'

        if incarcerated == NO:
            self.eligible = False
            self.reasons_ineligible = 'Woman is not incarcernated'

        if willing_to_consent == NO:
            self.eligible = False
            self.reasons_ineligible = 'Woman is not willing to provide'
            ' informed consent'
