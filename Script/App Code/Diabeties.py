import streamlit as st
import pickle as pk
import numpy as np

def page():
    set1,set2=st.columns([0.7,0.3])
    with set1:
        st.title("_Diabetes Prediction_")
    with set2:
        st.image("icon/diabetes.png",width=100)
    st.subheader("Please type in the below values: ")
    
    
    with st.form("HF_form"):
        col1,col2,col3=st.columns(3)
        with col1:
            Pregnancies=st.number_input("Pregnancies")
            SkinThickness=st.number_input("Skin Thickness")
            DiabetesPedigreeFunction=st.number_input("Diabetes Pedigree Function",format="%.3f")
        with col2:
            Glucose=st.number_input("Glucose")
            Insulin=st.number_input("Insulin")
            Age=st.number_input("Age")
        with col3:
            BloodPressure=st.number_input("BloodPressure")
            BMI=st.number_input("BMI")
        input_data=(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        submit=st.form_submit_button("Diagnose")
    
    if submit:
        system(input_data)

def system(input_data):
    load_scaler=pk.load(open("Sclae_Diabeties.sav",'rb'))
    load_model=pk.load(open("TM_Diabeties.sav",'rb'))
    cont=st.container(border=True)
    s=np.asanyarray(input_data)
    s=s.reshape(1,-1)
    s=load_scaler.transform(s)
    pred=load_model.predict(s)
    print(pred)
    if(pred[0]==0):
        cont.write("Result: :green[No chances of Diabetes]")
        cont.write("Recomendation: :blue[Your risk of diabetes is low, but maintaining a healthy lifestyle is essential. Continue eating a balanced diet, exercising regularly, and maintaining a healthy weight. Regular health check-ups and monitoring blood sugar levels can help detect any changes early. Avoiding excessive intake of sugary foods and drinks and managing stress are also beneficial for long-term health.]")
    else:
        cont.write("Result: :red[There is a chance of Diabetes]")
        cont.write("Recomendation:\n:blue[Given your high risk of diabetes, it's crucial to consult with a healthcare provider for further evaluation and management. Implementing lifestyle changes such as a balanced diet low in refined sugars, regular physical activity, maintaining a healthy weight, and monitoring blood sugar levels can significantly reduce your risk. Medications or insulin therapy might also be necessary as advised by your doctor. Regular check-ups and monitoring are essential to manage your condition effectively.]")
