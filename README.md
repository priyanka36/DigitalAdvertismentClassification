# DigitalAdvertismentClassification
A machine learning model used to perform multiclass-classification on various types of Jobs .

## How it works 
- You provide a text 
- It undergoes through various modules like preprocessing,vectorization and feature reduction and then predicts the output

## Required Libraries 
- TFIDF Vectorizer
- Truncated SVD 
- XGBOOST 

## How to run 
- Create new environment using conda : conda create -n env_name
- Install necessary dependencies : pip3 -r install requirements.txt
- CLone the repo : git clone https://github.com/priyanka36/DigitalAdvertismentClassification 
- To run the file through code : python3 main.py
- To run the file for demo using streamlit : streamlit run streamlit_app.py 

## File Structure : 
├── models
│   ├── finalized_model_RF.sav
│   |── finalized_model_XGB.sav
|   ├── svd.sav
|   |── vectorizer.sav
|
├── config.py
|__ helper_functions.py 
│__ requirements.txt
├── main.py
└── streamlit_app.py 





