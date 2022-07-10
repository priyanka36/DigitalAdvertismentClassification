import streamlit as st
from helper_functions import Inferencing
from config import model,feature_extraction_model,svd_model
import pandas as pd

st.header("Inferencing Digital Advertisment Classification")

txt = st.text_area("INPUT_TEXT_FOR_ANALYSIS",height=200,placeholder=None)
inference_obj = Inferencing()

if st.button('Predict'):

    cleaned_text = inference_obj.preprocessing(text)
    features = inference_obj.feature_extract(cleaned_text,feature_extraction_model,svd_model)
    predicted_output = inference_obj.predict_text(cleaned_text,features,model)
    st.write('**TEXT** :', predicted_output["text"]) 
    st.write('**LABEL** :',predicted_output["label_definition"]) 
    st.write('**SCORE** :', predicted_output["score"] )  
else:
    st.write('Press predict button to predict')

