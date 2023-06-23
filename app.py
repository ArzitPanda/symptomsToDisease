import numpy
import pandas
import pickle
import streamlit as st

sv = pickle.load(open('sv.pkl', 'rb'))
tfdid = pickle.load(open('tfdid.pkl', 'rb'))
res = {15: 'Psoriasis',
       17: 'Varicose Veins',
       16: 'Typhoid',
       4: 'Chicken pox',
       10: 'Impetigo',
       6: 'Dengue',
       8: 'Fungal infection',
       5: 'Common Cold',
       14: 'Pneumonia',
       7: 'Dimorphic Hemorrhoids',
       1: 'Arthritis',
       0: 'Acne',
       2: 'Bronchial Asthma',
       9: 'Hypertension',
       13: 'Migraine',
       3: 'Cervical spondylosis',
       11: 'Jaundice',
       12: 'Malaria',
       23: 'urinary tract infection',
       18: 'allergy',
       21: 'gastroesophageal reflux disease',
       20: 'drug reaction',
       22: 'peptic ulcer disease',
       19: 'diabetes'}
st.title("symptoms to disease")

a = st.text_input(placeholder="enter how to feel", label="symptoms")

if st.button("search"):
    feature = tfdid.transform([a])
    prediction = sv.predict(feature)[0]
    b = st.text(res[prediction])
    # st.write(res[prediction])
    if st.button("reset"):
        b.text("")


