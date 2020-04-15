from edc_constants.constants import NOT_APPLICABLE

from edc_list_data import PreloadData

list_data = {
    'td_maternal.chronicconditions': [
        ('Asthma', 'Asthma'),
        ('Hypertension', 'Hypertension'),
        ('Hypercholesterolemia', 'Hypercholesterolemia'),
        ('Heart disease', 'Heart disease'),
        ('Hepatitis B surface Ag positive', 'Hepatitis B surface Ag positive'),
        ('Chronic Hepatitis B carrier', 'Chronic Hepatitis B carrier'),
        ('Hepatitis C', 'Hepatitis C'),
        ('Diabetes', 'Diabetes'),
        ('Other, specify', 'Other, Specify'),
        ('Not Applicable', 'Not Applicable')
    ],
    'td_maternal.contraceptives': [
        ('Other, specify', 'Other, specify'),
        ('condom', 'Condom'),
        ('pill', 'Pills'),
        ('diapraghm', 'Diapraghm'),
        ('spemicide', 'Spemicide'),
        ('Oral contraceptive pills', 'Oral contraceptive pills'),
        ('Abstinence', 'Abstinence'),
        ('IUD', 'IUD'),
        ('tubilagation', 'Tubilagation'),
        ('Menstrual timing', 'Menstrual timing'),
        ('Withdrawal', 'Withdrawal'),
        ('Depo Provera (Injection)', 'Depo Provera (Injection)'),
        ('Hormonal Implant', 'Hormonal Implant'),
        ('Intrauterine Device', 'Intrauterine Device'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'td_maternal.covidsymptoms': [
        ('fever', 'Fever >37.5°C (99.5°F)'),
        ('chills', 'Chills'),
        ('nasal_congestion', 'Nasal Congestion'),
        ('sore_throat', 'Sore throat'),
        ('cough', 'Cough(new onset)'),
        ('shortness_of_breath', 'Shortness of breath (dyspnea)'),
        ('muscle_aches', 'Muscle aches (myalgia)'),
        ('nausea/vomiting', 'Nausea/vomiting'),
        ('diarrhea', 'Diarrhea'),
        ('abdominal_pain', 'Abdominal pain'),
        ('chest_pain', 'Chest pain'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'td_maternal.deliverycomplications': [
        ('Uterine rupture', 'Uterine rupture'),
        ('Hemorrhage req. transfusion', 'Hemorrhage req. transfusion'),
        ('Pre-eclampsia/eclampsia', 'Pre-eclampsia/eclampsia'),
        ('Placenta previa', 'Placenta previa'),
        ('Placental abruption', 'Placental abruption'),
        ('Chorioamnioitis or sus. chorioamnionitis',
         'Chorioamnioitis or sus. chorioamnionitis'),
        ('Intrapartum fever', 'Intrapartum fever'),
        ('Other', 'Other'),
        ('None', 'None')
    ],
    'td_maternal.foods': [
        ('Other fruits and vegetables', 'Other fruits and vegetables'),
        ('Eggs', 'Eggs'),
        ('Legumes and nuts', 'Legumes and nuts'),
        ('Dairy products (milk, yogurt, cheese)',
         'Dairy products (milk, yogurt, cheese)'),
        ('Flesh foods (meat, fish, poultry and liver/organ meat)',
         'Flesh foods (meat, fish, poultry and liver/organ meat)'),
        ('Vitamin A rich fruts and vegetables (carrots)',
         'Vitamin A rich fruits and vegetables (carrots)'),
        ('Grains, roots and tubers', 'Grains, roots and tubers'),
        ('Other', 'Other')
    ],
    'td_maternal.malformations': [
        ('Choroid Plexus Cyst', 'Choroid Plexus Cyst'),
        ('Intracranial Calcification', 'Intracranial Calcification'),
        ('Posterior Fossa Cyst', 'Posterior Fossa Cyst'),
        ('Intracranial Cyst', 'Intracranial Cyst'),
        ('Other, specify', 'Other, specify'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'td_maternal.maternaldiagnoseslist': [
        ('Pneumonia', 'Pneumonia'),
        ('Chlamydia', 'Chlamydia'),
        ('Tuberculosis', 'Tuberculosis'),
        ('Depression', 'Depression'),
        ('Pre-eclampsia', 'Pre-eclampsia'),
        ('Gonorrhea', 'Gonorrhea'),
        ('Liver Problems', 'Liver Problems'),
        ('Hepatitis C', 'Hepatitis C'),
        ('Syphillis', 'Syphillis'),
        ('Asthma requiring steroids', 'Asthma requiring steroids'),
        ('Genital Herpes', 'Genital Herpes'),
        ('Gestational Hypertension', 'Gestational Hypertension'),
        (NOT_APPLICABLE, 'Not Applicable'),
        ('Other, specify', 'Other, specify')
    ],
    'td_maternal.maternalhospitalization': [
        ('Pneumonia or other respiratory disease',
         'Pneumonia or other respiratory disease'),
        (NOT_APPLICABLE, 'Not Applicable'),
        ('Other, specify', 'Other, specify')
    ],
    'td_maternal.maternalmedications': [
        ('N/A', 'Not Applicable'),
        ('Cholesterol medications', 'Cholesterol medications'),
        ('Vitamin D supplement', 'Vitamin D supplement'),
        ('None', 'None'),
        ('Traditional medications', 'Traditional medications'),
        ('Hypertensive medications', 'Hypertensive medications'),
        ('Prenatal Vitamins', 'Prenatal Vitamins')
    ],
    'td_maternal.maternalrelatives': [
        ('Your mother', 'Your mother'),
        ('Your sister', 'Your sister'),
        ('Mother in law', 'Mother in law'),
        ('An auntie', 'An auntie'),
        ('No One', 'No One'),
        ('Other, specify', 'Other, specify')
    ],
    'td_maternal.priorarv': [
        ('AZT', 'AZT'),
        ('DDI', 'DDI'),
        ('Kaletra (or Aluvia)', 'Kaletra (or Aluvia)'),
        ('Nevirapine', 'Nevirapine'),
        ('3TC', '3TC'),
        ('Atripla', 'Atripla'),
        ('Tenofovir', 'Tenofovir'),
        ('Truvada (Tenofovir, FTC)', 'Truvada (Tenofovir, FTC)'),
        ('ATZ', 'ATZ'),
        ('D4T', 'D4T'),
        ('Raltegravir', 'Raltegravir'),
        ('Efavirenz (or Sustiva)', 'Efavirenz (or Sustiva)'),
        ('Combivir (AZT,3TC)', 'Combivir (AZT,3TC)'),
        ('Trizivir (AZT, 3TC, Abacavir)', 'Trizivir (AZT, 3TC, Abacavir)'),
        ('Abacavir', 'Abacavir'),
        ('Dolutegravir', 'DTG'),
        ('HAART, unknown', 'HAART, unknown'),
        (NOT_APPLICABLE, 'Not Applicable'),
        ('Other, specify', 'Other, specify')
    ],
    'td_maternal.rations': [
        ('Plumpy Nut', 'Plumpy Nut'),
        ('Cooking Oil', 'Cooking Oil'),
        ('Beans', 'Beans'),
        ('Infant Formula', 'Infant Formula'),
        ('Tsabana', 'Tsabana'),
        ('Other', 'Other')
    ],
    'td_maternal.wcsdxadult': [
        ('Asymptomatic', 'Asymptomatic'),
        ('Persistent generalized lymphadeno',
         'Persistent generalized lymphadeno'),
        ('Unexplained moderate weight loss',
         'Unexplained moderate weight loss'),
        ('Recurrent resp tract infection', 'Recurrent resp tract infection'),
        ('Herpes zoster', 'Herpes zoster'),
        ('Angular cheilitis', 'Angular cheilitis'),
        ('Recurrent oral ulceration', 'Recurrent oral ulceration'),
        ('Papular pruritic eruptions', 'Papular pruritic eruptions'),
        ('Seborrhoeic dermatitis', 'Seborrhoeic dermatitis'),
        ('Fungal nail infections', 'Fungal nail infections'),
        ('Unexplained* severe weight loss', 'Unexplained* severe weight loss'),
        ('Unexplained persistent fever', 'Unexplained persistent fever'),
        ('Unexplained chronic diarrhoea', 'Unexplained chronic diarrhoea'),
        ('Persistent oral candidiasis', 'Persistent oral candidiasis'),
        ('Oral hairy leukoplakia', 'Oral hairy leukoplakia'),
        ('Pulmonary tuberculosis', 'Pulmonary tuberculosis'),
        ('Severe bacterial infections', 'Severe bacterial infections'),
        ('stomatitis/gingivitis/periodontis',
         'Stomatitis/gingivitis/periodontis'),
        ('anaemia/neutropaenia/thrombocytopa',
         'Anaemia/neutropaenia/thrombocytopa'),
        ('HIV wasting syndrome', 'HIV wasting syndrome'),
        ('Pneumocystis pneumonia', 'Pneumocystis pneumonia'),
        ('Recurrent severe bacterial pneumo',
         'Recurrent severe bacterial pneumo'),
        ('Chronic herpes simplex infection',
         'Chronic herpes simplex infection'),
        ('Oesophageal candidiasis', 'Oesophageal candidiasis'),
        ('Extrapulmonary tuberculosis', 'Extrapulmonary tuberculosis'),
        ('Kaposi\u2019s sarcoma', 'Kaposi\u2019s sarcoma'),
        ('Cytomegalovirus infection', 'Cytomegalovirus infection'),
        ('CNS toxoplasmosis', 'CNS toxoplasmosis'),
        ('HIV encephalopathy', 'HIV encephalopathy'),
        ('Exp cryptococcosis/meningitis', 'Exp cryptococcosis/meningitis'),
        ('Diss non-TB mycobacterial infection',
         'Diss non-TB mycobacterial infection'),
        ('Prog multifocal leukoencephalopathy',
         'Prog multifocal leukoencephalopathy'),
        ('Chronic cryptosporidiosis', 'Chronic cryptosporidiosis'),
        ('Chronic isosporiasis', 'Chronic isosporiasis'),
        ('Disseminated mycosis', 'Disseminated mycosis'),
        ('Recurrent septicaemia', 'Recurrent septicaemia'),
        ('Lymphoma', 'Lymphoma'),
        ('Invasive cervical carcinoma', 'Invasive cervical carcinoma'),
        ('Atypical disseminated leishmaniasis',
         'Atypical disseminated leishmaniasis'),
        ('Sympt nephropathy/cardiomyopathy',
         'Sympt nephropathy/cardiomyopathy'),
        (NOT_APPLICABLE, NOT_APPLICABLE)
    ],
    'td_maternal.wcsdxped': [
        ('Asymptomatic', 'Asymptomatic'),
        ('Persistent gen lymphadenopathy', 'Persistent gen lymphadenopathy'),
        ('Unexp persistent hepatosplenomegaly',
         'Unexp persistent hepatosplenomegaly'),
        ('Papular pruritic eruptions', 'Papular pruritic eruptions'),
        ('Extensive wart virus infection', 'Extensive wart virus infection'),
        ('Extensive molluscum contagiosum', 'Extensive molluscum contagiosum'),
        ('Fungal nail infections', 'Fungal nail infections'),
        ('Recurrent oral ulcerations', 'Recurrent oral ulcerations'),
        ('Unexp persistent parotid enlargemen',
         'Unexp persistent parotid enlargement'),
        ('Lineal gingival erythema', 'Lineal gingival erythema'),
        ('Herpes zoster', 'Herpes zoster'),
        ('Chronic upper resp tract infections',
         'Chronic upper resp tract infections'),
        ('Unexplained** moderate malnutrition',
         'Unexplained** moderate malnutrition'),
        ('Unexplained persistent diarrhoea ',
         'Unexplained persistent diarrhoea'),
        ('Unexplained persistent fever ', 'Unexplained persistent fever'),
        ('Persistent oral candidiasis ', 'Persistent oral candidiasis'),
        ('Oral hairy leukoplakia', 'Oral hairy leukoplakia'),
        ('necrotiz ulcer gingivit/periodontis',
         'necrotiz ulcer gingivit/periodontis'),
        ('Lymph node tuberculosis', 'Lymph node tuberculosis'),
        ('Pulmonary tuberculosis', 'Pulmonary tuberculosis'),
        ('Severe recurrent bacterial pneumoni',
         'Severe recurrent bacterial pneumonia'),
        ('Symp lymph interstitial pneumonitis',
         'Symp lymph interstitial pneumonitis'),
        ('Chronic HIV-associated lung disease',
         'Chronic HIV-associated lung disease'),
        ('anaemia/neutropaenia/thrombocytopa',
         'anaemia/neutropaenia/thrombocytopa'),
        ('unexp sev wasting/stunting/mulnutri',
         'unexp sev wasting/stunting/mulnutrition'),
        ('Pneumocystis pneumonia', 'Pneumocystis pneumonia'),
        ('Recurr severe bacterial infections',
         'Recurrent severe bacterial infections'),
        ('Chronic herpes simplex infection ',
         'Chronic herpes simplex infection'),
        ('Extrapulmonary tuberculosis', 'Extrapulmonary tuberculosis'),
        ('Kaposi sarcoma', 'Kaposi sarcoma'),
        ('Oesophageal candidiasis ', 'Oesophageal candidiasis'),
        ('CNS toxoplasmosis', 'CNS toxoplasmosis'),
        ('HIV encephalopathy', 'HIV encephalopathy'),
        ('Cytomegalovirus infection', 'Cytomegalovirus infection'),
        ('Extrapulmonary cryptococcosis ', 'Extrapulmonary cryptococcosis'),
        ('Disseminated endemic mycosis ', 'Disseminated endemic mycosis'),
        ('Chronic cryptosporidiosis', 'Chronic cryptosporidiosis'),
        ('Chronic isosporiasis', 'Chronic isosporiasis'),
        ('Diss  non-TBmycobacterial infection',
         'Diss non-TBmycobacterial infection'),
        ('Cerebral/B-cell non-Hodgkin lymphom',
         'Cerebral/B-cell non-Hodgkin lymphom'),
        ('Prog multifocal leukoencephalopathy',
         'Prog multifocal leukoencephalopathy'),
        ('Sympt nephropathy/cardiomyopathy',
         'Sympt nephropathy/cardiomyopathy'),
        ('CS99999', 'CS99999'),
        (NOT_APPLICABLE, 'Not Applicable')]
}

preload_data = PreloadData(
    list_data=list_data)
