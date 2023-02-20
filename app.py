import streamlit as st
from PIL import Image
import pickle
import string
import re
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer 

ps = PorterStemmer()
image = Image.open('logo.png')

st.set_page_config(page_title = "CBDA", page_icon = image)
col1, col2 = st.columns([1,3.5], gap = "small")


with col1:
 
    st.image(image , use_column_width=True, output_format='auto')

with col2:

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
    st.title("Cyberbullying Detection Classifier")

    input_text = st.text_area("Enter the text to analyze")


    if st.button('Predict'):


    # 1. preprocess

        cleanText = clean_text(input_text)

        transformText = transform_text(cleanText)

    # 2. vectorize

        vector_input = tfidf.transform([transformText])
    # 3. predict

        result = model.predict(vector_input)[0]

    # 4. display

        if result == 1 :
            st.subheader("Result")
            st.markdown(":red[**_Cyberbullying_**]")
        else:
            st.subheader("Result")
            st.markdown(":green[**_Not Cyberbullying_**]")

        st.subheader("Original Text")
        st.text(input_text)
        st.subheader("Cleaned Text")
        st.text(cleanText)
        st.subheader("Transformed Text")
        st.text(transformText)
        st.subheader("Binary Prediction")
        if result == 1:
            st.markdown(":red["+ str(result) +"]")
        else:
            st.markdown(":green["+ str(result) +"]")

    
    
   