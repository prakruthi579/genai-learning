import streamlit as st
import pandas as pd

title=st.title("streamlit widgets")
st.write("give inputs")
name=st.text_input("Enter your name")
st.write(f"Hii {name}")
age=st.slider("enter your age",0,100,25)
st.write(f"Your age is {age}")
options=['male','female','others']
choice=st.selectbox("select your gender",options)
st.write(f"Your gender is {choice}")
email=st.text_input("enter your email")
data=pd.DataFrame({'name':[name],"age":[age],"gender":[choice],"email":[email]})
st.write(data)
csv_data=data.to_csv(index=False).encode('utf-8')
st.download_button(label="Download CSV",data=csv_data,file_name='user_data.csv',mime='text/csv')


file=st.file_uploader("upload a csv,pdf file",type=['csv','pdf'])

if file is not None:
    st.write(file.name)
    st.write("file uploaded successfully")