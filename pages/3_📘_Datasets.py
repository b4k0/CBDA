import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import io


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


st.set_page_config(page_title = "Datasets", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

 
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown(" <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2023 | Ioannis Bakomichalis</h1>", unsafe_allow_html=True)


st.title("Datasets📘")
st.markdown("---")
all_Datasets = ["Select a Dataset","Cyber Bullying Types Dataset", "Cyber Troll Dataset","Classified Tweets Dataset","Cyberbulling Classification Dataset","Cyber Bullying Types Dataset + Cyber Troll Dataset","Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset"]
data_choice = st.selectbox("Choose Dataset", all_Datasets)
st.markdown("---")
if data_choice == "Cyber Bullying Types Dataset":
    df_cyber = pd.read_csv("./Dataset/CyberBullyingTypesDataset.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_cyber.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_cyber.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_cyber.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_cyber.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_cyber
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_cyber.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_cyber.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_cyber.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_cyber[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_cyber.describe().T
        st.write(df_descr) 


    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Plots</h1>", unsafe_allow_html=True)

    class_dist = df_cyber["Class"].value_counts()

    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Bar Chart"):   
        st.bar_chart(class_dist, width=0, height=0 )

    if st.checkbox("Dataset Pie Chart"):   
        fig1, ax1 = plt.subplots()
        fig1.patch.set_facecolor('#0E1117')
        labels="Cyberstalking","Doxing","Revenge Porn", "Secual Harrssment", "Slut Shaming"
        ax1.pie(class_dist, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90, textprops={'color':"w"})
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
elif  data_choice == "Cyber Troll Dataset":
    df_cyber = pd.read_csv("./Dataset/cybertroll_dataset.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_cyber.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_cyber.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_cyber.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_cyber.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_cyber
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_cyber.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_cyber.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_cyber.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_cyber[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_cyber.describe().T
        st.write(df_descr) 


    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Plots</h1>", unsafe_allow_html=True)

    class_dist = df_cyber["annotation"].value_counts()

    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Bar Chart"):   
        st.bar_chart(class_dist, width=0, height=0 )

    if st.checkbox("Dataset Pie Chart"):   
        fig1, ax1 = plt.subplots()
        fig1.patch.set_facecolor('#0E1117')
        labels="Not Cyberbullying", "Cyberbullying"
        ax1.pie(class_dist, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90, textprops={'color':"w"})
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
elif  data_choice == "Classified Tweets Dataset":
    df_cyber = pd.read_csv("./Dataset/classified_tweets.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_cyber.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_cyber.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_cyber.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_cyber.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_cyber
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_cyber.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_cyber.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_cyber.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_cyber[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_cyber.describe().T
        st.write(df_descr) 


    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Plots</h1>", unsafe_allow_html=True)

    class_dist = df_cyber["cyberbullying"].value_counts()

    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Bar Chart"):   
        st.bar_chart(class_dist, width=0, height=0 )

    if st.checkbox("Dataset Pie Chart"):   
        fig1, ax1 = plt.subplots()
        fig1.patch.set_facecolor('#0E1117')
        labels="Not Cyberbullying", "Cyberbullying Level 1", "Cyberbullying Level 2 "
        ax1.pie(class_dist, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90, textprops={'color':"w"})
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
elif   data_choice == "Cyberbulling Classification Dataset": 
    df_cyber = pd.read_csv("./Dataset/cyberbullying_tweets.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_cyber.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_cyber.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_cyber.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_cyber.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_cyber
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_cyber.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_cyber.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_cyber.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_cyber[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_cyber.describe().T
        st.write(df_descr) 


    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Plots</h1>", unsafe_allow_html=True)

    class_dist = df_cyber["cyberbullying_type"].value_counts()

    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Bar Chart"):   
        st.bar_chart(class_dist, width=0, height=0 )

    if st.checkbox("Dataset Pie Chart"):   
        fig1, ax1 = plt.subplots()
        fig1.patch.set_facecolor('#0E1117')
        labels="Age","Ethnicity", "Gender", "Not Cyberbullying", "Other Cyberbullying", "Religion"
        ax1.pie(class_dist, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90, textprops={'color':"w"})
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
elif   data_choice == "Cyber Bullying Types Dataset + Cyber Troll Dataset":
    df_cyber = pd.read_csv("./Dataset/CyberTrollIEEE.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_cyber.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_cyber.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_cyber.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_cyber.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_cyber
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_cyber.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_cyber.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_cyber.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_cyber[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_cyber.describe().T
        st.write(df_descr) 


    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Plots</h1>", unsafe_allow_html=True)

    class_dist = df_cyber["annotation"].value_counts()

    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Bar Chart"):   
        st.bar_chart(class_dist, width=0, height=0 )

    if st.checkbox("Dataset Pie Chart"):   
        fig1, ax1 = plt.subplots()
        fig1.patch.set_facecolor('#0E1117')
        labels="Not Cyberbullying", "Cyberbullying"
        ax1.pie(class_dist, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90, textprops={'color':"w"})
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
elif  data_choice == "Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset": 
    df_cyber = pd.read_csv("./Dataset/cyberbullying.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_cyber.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_cyber.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_cyber.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_cyber.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_cyber
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_cyber.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_cyber.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_cyber.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_cyber[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_cyber.describe().T
        st.write(df_descr) 


    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Plots</h1>", unsafe_allow_html=True)

    class_dist = df_cyber["cyberbullying_type"].value_counts()

    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Bar Chart"):   
        st.bar_chart(class_dist, width=0, height=0 )

    if st.checkbox("Dataset Pie Chart"):   
        fig1, ax1 = plt.subplots()
        fig1.patch.set_facecolor('#0E1117')
        labels="Cyberbullying","Not Cyberbullying"
        ax1.pie(class_dist, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90, textprops={'color':"w"})
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)