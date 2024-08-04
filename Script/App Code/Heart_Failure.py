import streamlit as st
import pickle as pk
import numpy as np


def page():
    
    set1,set2=st.columns([0.7,0.3])
    with set1:
        st.title("_Heart Failure Prediction_")
    with set2:
        st.image("icon/heartbeat.png",width=100)
    st.subheader("Please type in the below values: ")
    

    with st.form("HF_form"):
        col1,col2,col3=st.columns(3)
        with col1:
            age=st.number_input("Age",min_value=0)
            DBP=st.number_input("Diastolic Blood Pressure",min_value=0)
            troponin=st.number_input("Troponin",format="%.3f",step=0.001)
        with col2:
            heart_rate=st.number_input("Heart rate",min_value=0)
            BS=st.number_input("Blood Sugar",min_value=0)
            
        with col3:
            SBP=st.number_input("Systolic Blood Pressure",min_value=0)
            CK_MB=st.number_input("CK-MB")

        input_data=(age,heart_rate,SBP,DBP,BS,CK_MB,troponin)
        submit=st.form_submit_button("Diagnose")
    if submit:
        system(input_data)

def system(input_data):
    load_model=pk.load(open("C:/Users/saran/OneDrive/Desktop/ML_DS project/TM_HeartAttack.sav",'rb'))
    cont=st.container(border=True)
    s=np.asanyarray(input_data)
    s=s.reshape(1,-1)
    pred=load_model.predict(s)
    print(pred)
    if(pred[0]==0):
        cont.write("Result: :green[There is no chance of heart attack]")
        cont.write("Recomendation: :blue[Your heart attack risk is low. Continue following a balanced diet, regular exercise, and maintain a healthy weight. Avoid smoking and limit alcohol intake. Regular health screenings and good mental well-being practices are important to keep your heart healthy.]")
    else:
        cont.write("Result: :red[There is a chance of heart attack]")
        cont.write("Recomendation:\n:blue[You have a high risk of a heart attack. Please consult a cardiologist immediately and consider medication adjustments. Adopt a heart-healthy diet, exercise regularly, maintain a healthy weight, quit smoking, and limit alcohol intake. Regular check-ups and stress management are also essential.]")
    
        



