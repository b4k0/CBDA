import streamlit as st
from PIL import Image



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


st.sidebar.markdown(" <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Ioannis Bakomichalis © 2023</h1>", unsafe_allow_html=True)




st.title("Algorithms📊")

all_Datasets = ["Select a Dataset","Cyber Bullying Types Dataset", "Cyber Troll Dataset","Classified Tweets Dataset","Cyberbulling Classification Dataset","Cyber Bullying Types Dataset + Cyber Troll Dataset","Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset"]
data_choice = st.selectbox("Choose Dataset", all_Datasets)
# all_Token = ["Tokenizing","Stemming", "Lemmatizing"]
# token_choice = st.selectbox("Choose Supplemental Data Cleaning", all_Token)
all_Vectorizers = ["Select a Vectorizer", "TF-IDF", "CountVectorizer"]
vect_choice = st.selectbox("Choose Vectorizer", all_Vectorizers)
all_ML_models = ["Select a Machine Learning Algorithm", "Logistic Regression", "Decision Tree", "Random Forest", "XGBoost", "Naive Bayes", "Support Vector Machine", "Bagging Decision Tree", "Boosting Decision Tree"]
model_choice = st.selectbox("Choose Machine Learning Algorithm", all_ML_models)

# if data_choice == "Select a Dataset":
#     st.warning(":white[You should select a **_Dataset_**]")
# elif vect_choice == "Select a Vectorizer":
#     st.warning(":white[You should select a **_Vectorizer_**]")
# elif model_choice == "Select a Machine Learning Algorithm":
#     st.warning(":white[You should select a **_Machine Learning Algorithm_**]")
if data_choice == "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Dataset_**]")
elif data_choice != "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Vectorizer_**]")
elif data_choice != "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Machine Learning Algorithm_**]")
elif data_choice == "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Dataset_** and **_Vectorizer_**]")
elif data_choice == "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Dataset_** and **_Machine Learning Algorithm_**]")
elif data_choice != "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Vectorizer_** and **_Machine Learning Algorithm_**]")
else:
    if data_choice == "Cyber Bullying Types Dataset":
    # if token_choice == "Tokenizing":
        if vect_choice == "TF-IDF":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.88%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_87.38%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.71%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_87.38%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_88.78%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.71%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_88.08%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_87.38%_**]")
        elif vect_choice == "CountVectorizer":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.65%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.71%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.18%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.95%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.88%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.88%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.25%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.01%_**]")
    elif   data_choice == "Cyber Troll Dataset":
        if vect_choice == "TF-IDF":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_76.08%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_85.92%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_91.70%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_76.00%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_78.20%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_80.50%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.87%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_91.22%_**]")
        elif vect_choice == "CountVectorizer":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_81.57%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.60%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_86.47%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_73.48%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_79.73%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_83.72%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_81.75%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.35%_**]")
    elif   data_choice == "Classified Tweets Dataset":
        if vect_choice == "TF-IDF":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.52%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.10%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_91.45%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.95%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_87.89%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_91.30%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_91.17%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.24%_**]")
        elif vect_choice == "CountVectorizer":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_91.07%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_88.90%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.92%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_91.38%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.39%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.24%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.95%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.40%_**]")
    elif   data_choice == "Cyberbulling Classification Dataset":  
        if vect_choice == "TF-IDF":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_86.10%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_82.23%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.12%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_86.26%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.67%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_86.27%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.61%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_83.54%_**]")
        elif vect_choice == "CountVectorizer":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_86.10%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_82.07%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.43%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_86.26%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.67%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_86.27%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.19%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_83.55%_**]")
    elif   data_choice == "Cyber Bullying Types Dataset + Cyber Troll Dataset":
        if vect_choice == "TF-IDF":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_78.12%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_85.45%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.29%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_75.52%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_79.95%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_80.60%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.84%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.06%_**]")
        elif vect_choice == "CountVectorizer":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_81.89%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_83.60%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_85.52%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_73.51%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_79.58%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_83.24%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_82.45%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.16%_**]")
    elif   data_choice == "Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset": 
        if vect_choice == "TF-IDF":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.57%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_80.03%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_81.77%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.50%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_74.90%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.72%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_82.69%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_80.65%_**]")
        elif vect_choice == "CountVectorizer":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.57%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_80.11%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_82.03%_**]")
            elif model_choice == "XGBoost":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.50%_**]")
            elif model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_74.90%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_84.72%_**]")
            elif model_choice == "Bagging Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_82.65%_**]")
            elif model_choice == "Boosting Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_80.48%_**]")

