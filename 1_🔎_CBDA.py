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


st.set_page_config(page_title = "CBDA", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

 
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Ioannis Bakomichalis © 2023</h1>", unsafe_allow_html=True)


def clean_text(tweet):
        # remove URL
        tweet = re.sub(r'http\S+', '', tweet)
        # Remove usernames
        tweet = re.sub(r'@[^\s]+[\s]?','',tweet)
        # Remove hashtags
        tweet = re.sub(r'#[^\s]+[\s]?','',tweet)
        # Remove emojis
        tweet = re.sub(r':[^\s]+[\s]?','',tweet)
        # remove special characters
        tweet = re.sub('[^ a-zA-Z0-9]' , '', tweet)
        # remove RT
        tweet = re.sub('RT' , '', tweet)
        # remove Numbers
        tweet = re.sub('[0-9]', '', tweet)

        return tweet

def transform_text(text):
        text = text.lower()
        text = nltk.word_tokenize(text)

        y=[]
        for i in text:
            if i.isalnum():
                y.append(i)

        text = y[:]
        y.clear()

        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)

        text = y[:]
        y.clear()

        for i in text:
                y.append(ps.stem(i))

        return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
image = Image.open('logo.png')

    # st.set_page_config(page_title = "CBDA", page_icon = image)

    # st.image(image , use_column_width=True, output_format='auto')

st.title("Cyber Bullying Detection ")

input_text = st.text_area("**_Enter the text to analyze_**")



if st.button('Predict'):
    if input_text == "":
     st.snow()
     st.warning("Please provide some text!")
    else:
        with st.spinner("**_Prediction_** in progress. Please wait 🙏"):
            time.sleep(3)
    # 1. preprocess

        cleanText = clean_text(input_text)

        transformText = transform_text(cleanText)

    # 2. vectorize

        vector_input = tfidf.transform([transformText])
    # 3. predict

        result = model.predict(vector_input)[0]


    # 4. display
        st.markdown("---")
        if result == 1 :
            st.subheader("Result")
            st.error(":red[**_Cyberbullying_**]")
        else:
            st.subheader("Result")
            st.success(":green[**_Not Cyberbullying_**]")
        st.markdown("---")
        st.subheader("Original Text")
        st.text(input_text)
        st.markdown("---")
        st.subheader("Cleaned Text")
        st.text(cleanText)
        st.markdown("---")
        st.subheader("Transformed Text")
        st.text(transformText)
        st.markdown("---")
        st.subheader("Binary Prediction")
        if result == 1:
            st.markdown(":red["+ str(result) +"]")
        else:
            st.markdown(":green["+ str(result) +"]")
        st.markdown("---")

    
    
   