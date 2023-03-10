import streamlit as st
from PIL import Image
import pickle
import string
import re
import time


hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('logo.png')


st.set_page_config(page_title = "Algorithms", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

 
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Ioannis Bakomichalis © 2023</h1>", unsafe_allow_html=True)




st.title("Algorithms📊")

all_Datasets = ["IEEE", "Cyber Troll","Classified Tweets","Cyberbulling Tweets","IEEE + Cyber Troll","IEEE + Cyber Troll + Classified Tweets + Cyberbulling Tweets"]
vect_choice = st.selectbox("Choose Dataset", all_Datasets)
all_Token = ["Tokenizing","Stemming", "Lemmatizing"]
vect_choice = st.selectbox("Choose Supplemental Data Cleaning", all_Token)
all_Vectorizers = ["TF-IDF", "Count Vectorizer"]
vect_choice = st.selectbox("Choose Vectorizer", all_Vectorizers)
all_ML_models = ["Logistic Regression", "Decision Tree", "Random Forest", "XGBoost", "Naive Bayes", "Support Vector Machine", "Bagging Decision Tree", "Boosting Decision Tree"]
model_choice = st.selectbox("Choose Machine Learning Algorithm", all_ML_models)