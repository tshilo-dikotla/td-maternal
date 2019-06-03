from edc_constants.constants import YES, NO


class KaraboEligibility:

    infant_bith_data = 'td_infant.infantbirthdata'

    def __init__(self, model_obj=None):

        self.eligible = True
        self.reasons_ineligible = []
        self.subject_identifier = model_obj.subject_identifier

        if model_obj.infant_alive == NO:
            self.eligible = False
            self.reasons_ineligible.append('Infant is not alive.')

        if model_obj.infant_weight == NO:
            self.eligible = False
            self.reasons_ineligible.append('Infant weight < 2.00 kilograms.')

        if model_obj.major_anomalies == YES:
            self.eligible = False
            self.reasons_ineligible.append('Infant was born with major'
                                           ' congenital anomalies.')

        if model_obj.birth_complications == YES:
            self.eligible = False
            self.reasons_ineligible.append(
                'Infant experienced birth complications.')

        if model_obj.infant_documentation == NO:
            self.eligible = False
            self.reasons_ineligible.append(
                'Infant does not have documentation that'
                ' they received a BCG vaccine within 72 hours of birth'
                ' in the Under 5 Health.')

        if model_obj.infant_months == YES:
            self.eligible = False
            self.reasons_ineligible.append(
                'Infant has reached 21 months of age.')

        if model_obj.tb_treatment == YES:
            self.eligible = False
            self.reasons_ineligible.append('Woman was in tb treatment'
                                           ' during pregnancy.')

        if model_obj.incarcerated == YES:
            self.eligible = False
            self.reasons_ineligible.append('Woman is incarcerated.')

        if model_obj.willing_to_consent == NO:
            self.eligible = False
            self.reasons_ineligible.append('Woman is not willing to provide'
                                           ' informed consent.')
