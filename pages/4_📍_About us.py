import streamlit as st
from PIL import Image
import pickle
import string
import re
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer 
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
ps = PorterStemmer()
image = Image.open('logo.png')


st.set_page_config(page_title = "About us", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

 
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Ioannis Bakomichalis © 2023</h1>", unsafe_allow_html=True)




st.title("About us📍")
st.markdown("<br> <br> ", unsafe_allow_html=True)

st.markdown("The project **_CBDA_** developed by Postgraduate student :blue[**_Ioannis Bakomichalis_**] for his MSc Dissertation :blue[**_Cyberbullying Detection through NLP & Machine Learning_**].")
st.markdown("<br> <br> ", unsafe_allow_html=True)
st.markdown("<br> <br> ", unsafe_allow_html=True)
st.markdown("<br> <br>", unsafe_allow_html=True)
col1, col2 = st.columns([2,4])
with col1:
    image = Image.open('unipiLogo.png')
    st.image(image, use_column_width=False, output_format='auto')
with col2:
    st.markdown("<br> ", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 15px; color: #002d51;'>University of Piraeus, Department of Digital Systems</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 15px; color: #002d51;'>MSc Digital Systems Security</h1>", unsafe_allow_html=True)