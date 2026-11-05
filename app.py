import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler,OneHotEncoder
import pickle
import tensorflow as tf
model=tf.keras.models.load_model('model.h5')
with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender=pickle.load(file)
with open('onehot_encoder_geo.pkl','rb')as file:
    onehot_encoder_geo=pickle.load(file)
with open('Scaler.pkl','rb') as file:
    Scaler=pickle.load(file)
st.title("Customer Churn Prediction")
geography=st.selectbox('Geography',onehot_encoder_geo.categories_[0])
gender=st.selectbox('gender',label_encoder_gender.classes_)
age=st.slider('Age',18,92)
balance=st.number_input('Balance')
credit_score=st.number_input("credit score")
estimated_salary=st.number_input('Estimated salary')
tenure=st.slider('Tenure',0,10)
num_of_products=st.slider('Number of products',1,4)
has_cr_card=st.selectbox('Has Credit card',[0,1])
is_active_member=st.selectbox('IS Active Member',[0,1])

input_data=pd.DataFrame({
    'CreditScore':[credit_score],'Gender':[label_encoder_gender.transform([gender])[0]],'Age':[age],
    'Tenure':[tenure],'Balance':[balance],'NumOfProducts':[num_of_products],'HasCrCard':[has_cr_card],
    'IsActiveMember':[is_active_member],'EstimatedSalary':[estimated_salary]
})
geo_encoder=onehot_encoder_geo.transform([[geography]])
geo_encoded_df=pd.DataFrame(geo_encoder,columns=onehot_encoder_geo.get_feature_names_out(['Geography']))
input_data=pd.concat([input_data.reset_index(drop=True),geo_encoded_df],axis=1)
input_data_scaled=Scaler.transform(input_data)
p=model.predict(input_data_scaled)
prediction_prob=p[0][0]
st.write(f"churn probability:{prediction_prob:.2f}")
if prediction_prob>0.5:
    st.write('the customer is likely to churn')
else:
    st.write("the customer is not likely to churn")