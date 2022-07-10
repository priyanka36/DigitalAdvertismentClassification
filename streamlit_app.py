import streamlit as st
from helper_functions import Inferencing
from config import model,feature_extraction_model,svd_model
import pandas as pd

st.header("Inferencing Digital Advertisment Classification")

txt = st.text_area("INPUT_TEXT_FOR_ANALYSIS",height=200,placeholder=None)
inference_obj = Inferencing()
text = "jobsjobs in new york nyjava backend developer jobs in new york nyjun 05 2022contact namechristopher10292new york nyunited states0 32 yearsjob openings are available across usdoc docx pdf extensions are supported0500get best matching jobs through email mandatorydoc docx pdf extensions are supported05000 16 years0 16 years0 40 years0 18 yearsstellent it llcjersey city nj usrhp soft incnew york ny uspayoneernew york ny usavtech solutionsfranklin lakes nj useuleritynew york ny ussnakorpio group incwayne nj uspegasus knowledge solutionsnew york ny usinfovision incpiscataway nj us0 40 years0 2 yearsget best matching jobs through email mandatoryxxneed job hiring"

if st.button('Predict'):

    cleaned_text = inference_obj.preprocessing(text)
    features = inference_obj.feature_extract(cleaned_text,feature_extraction_model,svd_model)
    predicted_output = inference_obj.predict_text(cleaned_text,features,model)
    st.write('**TEXT** :', predicted_output["text"]) 
    st.write('**LABEL** :',predicted_output["label_definition"]) 
    st.write('**SCORE** :', predicted_output["score"] )  
else:
    st.write('Press predict button to predict')

