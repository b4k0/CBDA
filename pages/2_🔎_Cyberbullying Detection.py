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


st.set_page_config(page_title = "Cyberbullying Detection", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2023 | Ioannis Bakomichalis</h1>", unsafe_allow_html=True)


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

tfidf = pickle.load(open('TFIDFvectorizer.pkl','rb'))
model = pickle.load(open('bestmodel.pkl','rb'))
image = Image.open('logo.png')

st.title("Cyber-Bullying Detection🔍")

input_text = st.text_area("**_Enter the text to analyze_**", key="**_Enter the text to analyze_**")
col1, col2 = st.columns([1,6])
with col1:
    button_predict = st.button('Predict')
with col2:

    def clear_text():
        st.session_state["**_Enter the text to analyze_**"] = ""

    # clear button
    button_clear = st.button("Clear", on_click=clear_text)
    
    # predict button animations
if button_predict:
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

        # result2 = model.predict_proba(vector_input)[0] 
        #clf=svm.SVC(probability=True)


    # 4. display
        st.markdown("---")
        if result == 1 :
            st.subheader("Result")
            st.error(":red[**_Cyberbullying_**]")
            # st.markdown(result2)
        else:
            st.subheader("Result")
            st.success(":green[**_Not Cyberbullying_**]")
            # st.markdown(result2)
        st.markdown("---")
        st.subheader("Original Text")
        expander_original = st.expander("Information", expanded=False)
        with expander_original:
            st.info("The text that the user provided!")
        st.text(input_text)
        st.markdown("---")
        st.subheader("Cleaned Text")
        expander_clean = st.expander("Information", expanded=False)
        with expander_clean:
            st.info("From original text has removed punctuation and special characters. Also it has removed hashtags, tags and emojis!")
        st.text(cleanText)
        st.markdown("---")
        st.subheader("Transformed Text")
        expander_transform = st.expander("Information", expanded=False)
        with expander_transform:
            st.info("From Cleaned text has removed stopwords and transformed to lowercase. Also, it has be used Stemming!")
        st.text(transformText)
        st.markdown("---")
        st.subheader("Binary Prediction")
        expander_binary = st.expander("Information", expanded=False)
        with expander_binary:
            st.info("Binary Prediction from the Model!")
        if result == 1:
            st.markdown(":red["+ str(result) +"]")
        else:
            st.markdown(":green["+ str(result) +"]")
        st.markdown("---")
        st.subheader("Model Accuracy")
        expander_accuracy = st.expander("Information", expanded=False)
        with expander_accuracy:
            st.info("Model Accuracy using Random Forest (RF) Classifier!")
        st.warning("Accuracy:  **_91.70 %_**")
        st.markdown("---")