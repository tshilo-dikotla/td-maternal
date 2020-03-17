from edc_constants.constants import YES, NO


class KaraboEligibility:

    infant_bith_data = 'td_infant.infantbirthdata'

    def __init__(self, model_obj=None):

        self.eligible = True
        self.reasons_ineligible = []
        self.subject_identifier = model_obj.subject_identifier

        if model_obj.infant_alive == NO:
            self.eligible = False
            self.reasons_ineligible.append('Infant not alive.')

        if model_obj.infant_weight == NO:
            self.eligible = False
            self.reasons_ineligible.append('Low birth weight.')

        if model_obj.major_anomalies == YES:
            self.eligible = False
            self.reasons_ineligible.append('Congenital anomalies.')

        if model_obj.birth_complications == YES:
            self.eligible = False
            self.reasons_ineligible.append('Birth complications.')

        if model_obj.infant_documentation == NO:
            self.eligible = False
            self.reasons_ineligible.append('BCG documentation')

        if model_obj.infant_months == YES:
            self.eligible = False
            self.reasons_ineligible.append('Too old')

        if model_obj.tb_treatment == YES:
            self.eligible = False
            self.reasons_ineligible.append('Maternal TB treatment')

        if model_obj.incarcerated == YES:
            self.eligible = False
            self.reasons_ineligible.append('Maternal incarceration')

        if model_obj.willing_to_consent == NO:
            self.eligible = False
            self.reasons_ineligible.append('Maternal Consent')
