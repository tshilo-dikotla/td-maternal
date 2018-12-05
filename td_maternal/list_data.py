from edc_constants.constants import NOT_APPLICABLE, OTHER

from edc_list_data import PreloadData


list_data = {
    'td_maternal.chronicconditions': [
        ('asthma', 'Asthma'),
        ('hypertension', 'Hypertension'),
        ('hypercholesterolemia', 'Hypercholesterolemia'),
        ('heart_disease', 'Heart disease'),
        ('hepatitis_b_surface_ag_positive', 'Hepatitis B surface Ag positive'),
        ('chronic_hepatitis_b_carrier', 'Chronic Hepatitis B carrier'),
        ('hepatitis_c', 'Hepatitis C'),
        ('diabetes', 'Diabetes'),
        (OTHER, 'Other, Specify'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'td_maternal.contraceptives': [
        (OTHER, 'Other, specify'),
        ('condom', 'Condom'),
        ('pills', 'Pills'),
        ('diapraghm', 'Diapraghm'),
        ('spemicide', 'Spemicide'),
        ('oral_contraceptive_pills', 'Oral contraceptive pills'),
        ('abstinence', 'Abstinence'),
        ('iud', 'IUD'),
        ('menstrual_timing', 'Menstrual timing'),
        ('withdrawal', 'Withdrawal'),
        ('depo_provera_injection', 'Depo Provera (Injection)'),
        ('hormonal_implant', 'Hormonal Implant'),
        ('intrauterine_device', 'Intrauterine Device'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'td_maternal.deliverycomplications': [
        ('uterine_rupture', 'Uterine rupture'),
        ('hemorrhage_req._transfusion', 'Hemorrhage req. transfusion'),
        ('pre_eclampsia_eclampsia', 'Pre-eclampsia/eclampsia'),
        ('placenta_previa', 'Placenta previa'),
        ('placental_abruption', 'Placental abruption'),
        ('chorioamnioitis', 'Chorioamnioitis or sus. chorioamnionitis'),
        ('intrapartum_fever', 'Intrapartum fever'),
        (OTHER, 'Other')
    ],
    'td_maternal.foods': [
        ('other_fruits_vegetables', 'Other fruits and vegetables'),
        ('eggs', 'Eggs'),
        ('legumes_and_nuts', 'Legumes and nuts'),
        ('diary_products', 'Dairy products (milk, yogurt, cheese)'),
        ('flesh_foods',
         'Flesh foods (meat, fish, poultry and liver/organ meat)'),
        ('vitamin_a_fruits_vegetables',
         'Vitamin A rich fruits and vegetables (carrots)'),
        ('grains_roots_tubers', 'Grains, roots and tubers'),
        (OTHER, 'Other')
    ],
    'td_maternal.malformations': [
        ('choroid_plexus_cyst', 'Choroid Plexus Cyst'),
        ('intracranial_calcification', 'Intracranial Calcification'),
        ('posterior_fossa_cyst', 'Posterior Fossa Cyst'),
        ('intracranial_cyst', 'Intracranial Cyst'),
        (OTHER, 'Other, specify'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'td_maternal.maternaldiagnoseslist': [
        ('pneumonia', 'Pneumonia'),
        ('chlamydia', 'Chlamydia'),
        ('tuberculosis', 'Tuberculosis'),
        ('depression', 'Depression'),
        ('pre_eclampsia', 'Pre-eclampsia'),
        ('gonorrhea', 'Gonorrhea'),
        ('liver_problems', 'Liver Problems'),
        ('hepatitis_c', 'Hepatitis C'),
        ('syphillis', 'Syphillis'),
        ('asthma_requiring_steroids', 'Asthma requiring steroids'),
        ('genital_herpes', 'Genital Herpes'),
        ('gestational_hypertension', 'Gestational Hypertension'),
        (NOT_APPLICABLE, 'Not Applicable'),
        (OTHER, 'Other, specify')
    ],
    'td_maternal.maternalhospitalization': [
        ('pneumonia_or_other_respiratory_disease',
         'Pneumonia or other respiratory disease'),
        (NOT_APPLICABLE, 'Not Applicable'),
        (OTHER, 'Other, specify')
    ],
    'td_maternal.maternalmedications': [
        ('cholesterol_medications', 'Cholesterol medications'),
        ('vitamin_d_supplement', 'Vitamin D supplement'),
        ('traditional_medications', 'Traditional medications'),
        ('hypertensive_medications', 'Hypertensive medications'),
        ('prenatal_vitamins', 'Prenatal Vitamins'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'td_maternal.maternalrelatives': [
        ('your_mother', 'Your mother'),
        ('your_sister', 'Your sister'),
        ('mother_in_law', 'Mother in law'),
        ('an_auntie', 'An auntie'),
        ('no_one', 'No One'),
        (OTHER, 'Other, specify')
    ],
    'td_maternal.priorarv': [
        ('azt', 'AZT'),
        ('ddi', 'DDI'),
        ('kaletra_or_aluvia', 'Kaletra (or Aluvia)'),
        ('nevirapine', 'Nevirapine'),
        ('3tc', '3TC'),
        ('atripla', 'Atripla'),
        ('tenofovir', 'Tenofovir'),
        ('truvada_tenofovir_ftc', 'Truvada (Tenofovir, FTC)'),
        ('atz', 'ATZ'),
        ('d4t', 'D4T'),
        ('raltegravir', 'Raltegravir'),
        ('efavirenz_or_sustiva', 'Efavirenz (or Sustiva)'),
        ('combivir_azt_3tc', 'Combivir (AZT,3TC)'),
        ('trizivir_azt_3tc_abacavir', 'Trizivir (AZT, 3TC, Abacavir)'),
        ('abacavir', 'Abacavir'),
        ('haart_unknown', 'HAART, unknown'),
        (NOT_APPLICABLE, 'Not Applicable'),
        (OTHER, 'Other, specify')
    ],
    'td_maternal.rations': [
        ('plumpy_nut', 'Plumpy Nut'),
        ('cooking_oil', 'Cooking Oil'),
        ('beans', 'Beans'),
        ('infant_formula', 'Infant Formula'),
        ('tsabana', 'Tsabana'),
        (OTHER, 'Other')
    ],
    'td_maternal.wcsdxadult': [
        ('asymptomatic', 'Asymptomatic'),
        ('persistent_generalized_lymphadeno',
         'Persistent generalized lymphadeno'),
        ('unexplained_moderate_weight_loss',
         'Unexplained moderate weight loss'),
        ('recurrent_resp_tract_infection', 'Recurrent resp tract infection'),
        ('herpes_zoster', 'Herpes zoster'),
        ('angular_cheilitis', 'Angular cheilitis'),
        ('recurrent_oral_ulceration', 'Recurrent oral ulceration'),
        ('papular_pruritic_eruptions', 'Papular pruritic eruptions'),
        ('seborrhoeic_dermatitis', 'Seborrhoeic dermatitis'),
        ('fungal_nail_infections', 'Fungal nail infections'),
        ('unexplained_severe_weight_loss', 'Unexplained* severe weight loss'),
        ('unexplained_persistent_fever', 'Unexplained persistent fever'),
        ('unexplained_chronic_diarrhoea', 'Unexplained chronic diarrhoea'),
        ('persistent_oral_candidiasis', 'Persistent oral candidiasis'),
        ('oral_hairy_leukoplakia', 'Oral hairy leukoplakia'),
        ('pulmonary_tuberculosis', 'Pulmonary tuberculosis'),
        ('severe_bacterial_infections', 'Severe bacterial infections'),
        ('stomatitis_or_gingivitis_or_periodontis',
         'Stomatitis/gingivitis/periodontis'),
        ('anaemia_or_neutropaenia_or_thrombocytopa',
         'Anaemia/neutropaenia/thrombocytopa'),
        ('hiv_wasting_syndrome', 'HIV wasting syndrome'),
        ('pneumocystis_pneumonia', 'Pneumocystis pneumonia'),
        ('recurrent_severe_bacterial_pneumo',
         'Recurrent severe bacterial pneumo'),
        ('chronic_herpes_simplex_infection',
         'Chronic herpes simplex infection'),
        ('oesophageal_candidiasis', 'Oesophageal candidiasis'),
        ('extrapulmonary_tuberculosis', 'Extrapulmonary tuberculosis'),
        ('kaposi_u2019s_sarcoma', 'Kaposi\u2019s sarcoma'),
        ('cytomegalovirus_infection', 'Cytomegalovirus infection'),
        ('cns_toxoplasmosis', 'CNS toxoplasmosis'),
        ('hiv_encephalopathy', 'HIV encephalopathy'),
        ('exp_cryptococcosis_or_meningitis', 'Exp cryptococcosis/meningitis'),
        ('diss_non_TB_mycobacterial_infection',
         'Diss non-TB mycobacterial infection'),
        ('prog_multifocal_leukoencephalopathy',
         'Prog multifocal leukoencephalopathy'),
        ('chronic_cryptosporidiosis', 'Chronic cryptosporidiosis'),
        ('chronic_isosporiasis', 'Chronic isosporiasis'),
        ('disseminated_mycosis', 'Disseminated mycosis'),
        ('recurrent_septicaemia', 'Recurrent septicaemia'),
        ('lymphoma', 'Lymphoma'),
        ('invasive_cervical_carcinoma', 'Invasive cervical carcinoma'),
        ('atypical_disseminated_leishmaniasis',
         'Atypical disseminated leishmaniasis'),
        ('sympt_nephropathy_or_cardiomyopathy',
         'Sympt nephropathy/cardiomyopathy'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'td_maternal.wcsdxped': [
        ('asymptomatic', 'Asymptomatic'),
        ('persistent_gen_lymphadenopathy', 'Persistent gen lymphadenopathy'),
        ('unexp_persistent_hepatosplenomegaly',
         'Unexp persistent hepatosplenomegaly'),
        ('papular_pruritic_eruptions', 'Papular pruritic eruptions'),
        ('extensive_wart_virus_infection', 'Extensive wart virus infection'),
        ('extensive_molluscum_contagiosum', 'Extensive molluscum contagiosum'),
        ('fungal_nail_infections', 'Fungal nail infections'),
        ('recurrent_oral_ulcerations', 'Recurrent oral ulcerations'),
        ('unexp_persistent_parotid_enlargement',
         'Unexp persistent parotid enlargement'),
        ('lineal_gingival_erythema', 'Lineal gingival erythema'),
        ('herpes_zoster', 'Herpes zoster'),
        ('chronic_upper_resp_tract_infections',
         'Chronic upper resp tract infections'),
        ('unexplained_moderate_malnutrition',
         'Unexplained** moderate malnutrition'),
        ('unexplained_persistent_diarrhoea',
         'Unexplained persistent diarrhoea'),
        ('unexplained_persistent_fever', 'Unexplained persistent fever'),
        ('persistent_oral_candidiasis', 'Persistent oral candidiasis'),
        ('oral_hairy_leukoplakia', 'Oral hairy leukoplakia'),
        ('necrotiz_ulcer_gingivit_or_periodontis',
         'necrotiz ulcer gingivit/periodontis'),
        ('lymph_node_tuberculosis', 'Lymph node tuberculosis'),
        ('pulmonary_tuberculosis', 'Pulmonary tuberculosis'),
        ('severe_recurrent_bacterial_pneumonia',
         'Severe recurrent bacterial pneumonia'),
        ('symp_lymph_interstitial_pneumonitis',
         'Symp lymph interstitial pneumonitis'),
        ('chronic_HIV-associated_lung_disease',
         'Chronic HIV-associated lung disease'),
        ('anaemia_or_neutropaenia_or_thrombocytopa',
         'anaemia/neutropaenia/thrombocytopa'),
        ('unexp_sev_wasting/stunting/mulnutrition',
         'unexp sev wasting/stunting/mulnutrition'),
        ('pneumocystis_pneumonia', 'Pneumocystis pneumonia'),
        ('recurr_severe_bacterial_infections',
         'Recurrent severe bacterial infections'),
        ('chronic_herpes_simplex_infection',
         'Chronic herpes simplex infection'),
        ('extrapulmonary_tuberculosis', 'Extrapulmonary tuberculosis'),
        ('kaposi_sarcoma', 'Kaposi sarcoma'),
        ('qesophageal_candidiasis', 'Oesophageal candidiasis'),
        ('CNS_toxoplasmosis', 'CNS toxoplasmosis'),
        ('HIV_encephalopathy', 'HIV encephalopathy'),
        ('cytomegalovirus_infection', 'Cytomegalovirus infection'),
        ('extrapulmonary_cryptococcosis', 'Extrapulmonary cryptococcosis'),
        ('disseminated_endemic_mycosis', 'Disseminated endemic mycosis'),
        ('chronic_cryptosporidiosis', 'Chronic cryptosporidiosis'),
        ('chronic_isosporiasis', 'Chronic isosporiasis'),
        ('diss_non_TBmycobacterial_infection',
         'Diss non-TBmycobacterial infection'),
        ('cerebral_B_cell_non_Hodgkin_lymphom',
         'Cerebral/B-cell non-Hodgkin lymphom'),
        ('prog_multifocal_leukoencephalopathy',
         'Prog multifocal leukoencephalopathy'),
        ('sympt_nephropathy_or_cardiomyopathy',
         'Sympt nephropathy/cardiomyopathy'),
        ('CS99999', 'CS99999'),
        (NOT_APPLICABLE, 'Not Applicable')]
}

preload_data = PreloadData(
    list_data=list_data)
