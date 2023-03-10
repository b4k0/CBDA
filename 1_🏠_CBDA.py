import streamlit as st
from PIL import Image
import pickle
import string
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer 
import time

hide_menu = """
<style>


footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
ps = PorterStemmer()
image = Image.open('logo.png')


st.set_page_config(page_title = "CBDA", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Ioannis Bakomichalis © 2023</h1>", unsafe_allow_html=True)

st.image(image , use_column_width=True, output_format='auto')

st.markdown("---")

st.markdown("<h1 style='text-align: center; font-size: 25px; color: #FFFFFF;'>The Ultimate Web Application for Cyberbullying Detection</h1>", unsafe_allow_html=True)