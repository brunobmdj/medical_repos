import streamlit as st
st.title('Medical Diagnostic Web App')
st.subheader('Is the patient Diabetic')
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler


# Step1: Load the pickled model

model = open('rfc.pickle','rb') # read binary
clf = pickle.load(model)
model.close()

# Step2: Get input from front end user

pregs = st.number_input('Pregnancies',0,17,0) 
glucose = st.slider('Glucose',40,200,40)
bp= st.slider('BloodPressure',20,140,20) 
skin= st.slider('SkinThickness',7.0,99.0,7.0) 
insulin= st.slider('Insulin',14,850,14)
bmi = st.slider('BMI',18,67,18)
dpf = st.slider('DiabetesPedigreeFunction',0.05,2.50,0.05)
age = st.slider('Age',20,90,20)

# Step3: Collect the front end user input as model input data

data = {'Pregnancies':pregs, 
        'Glucose':glucose, 
        'BloodPressure':bp, 
        'SkinThickness':skin, 
        'Insulin':insulin,
        'BMI':bmi, 
        'DiabetesPedigreeFunction':dpf, 
        'Age':age}
input_data = pd.DataFrame([data])

# Step4: get the predictions and print the result

preds=clf.predict(input_data)[0]
if st.button('Predict'):
    if preds==1:
        st.error('Diabetic')
    if preds==0:
        st.error('Non Diabetic')
