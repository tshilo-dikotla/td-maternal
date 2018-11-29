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
    ],
}

preload_data = PreloadData(
    list_data=list_data)
