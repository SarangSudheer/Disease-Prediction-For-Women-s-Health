import streamlit as st
import pickle as pk
import numpy as np

def page():
    
    set1,set2=st.columns([0.7,0.3])
    with set1:
        st.title("_Breast Cancer Prediction_")
    with set2:
        st.image("icon/cancer-ribbon.png",width=100)
    st.subheader("Please type in the below values: ")
    

    with st.form("HF_form"):
        col1,col2,col3=st.columns(3)
        with col1:
            radius_mean=st.number_input("radius mean")
            area_mean=st.number_input("area mean")
            concavity_mean=st.number_input("concavity mean",format="%.5f",step=0.00001)
            fractal_dimension_mean=st.number_input("fractal_dimension_mean",format="%.5f",step=0.00001)
        with col2:
            texture_mean=st.number_input("texture mean")
            smoothness_mean=st.number_input("smoothness mean",format="%.5f",step=0.00001)
            concave_points_mean=st.number_input("concave points mean",format="%.5f",step=0.00001)
        with col3:
            perimeter_mean=st.number_input("perimeter mean")
            compactness_mean=st.number_input("compactness mean",format="%.5f",step=0.00001)
            symmetry_mean=st.number_input("symmetry mean",format="%.5f",step=0.00001)
        input_data=(radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean)
        submit=st.form_submit_button("Diagnose")
    if submit:
        system(input_data)

def system(input_data):
    load_scaler=pk.load(open("Sclae_BreastCancer.sav",'rb'))
    load_model=pk.load(open("TM_BreastCancer.sav",'rb'))
    cont=st.container(border=True)
    s=np.asanyarray(input_data)
    s=s.reshape(1,-1)
    s=load_scaler.transform(s)
    pred=load_model.predict(s)
    print(pred)
    if(pred[0]=="B"):
        cont.write("Result: :green[No chances of Breast Cancer]")
        cont.write("Recomendation: :blue[Your risk of breast cancer is low, but it's important to continue with regular screenings and maintain a healthy lifestyle. Eat a balanced diet, exercise regularly, limit alcohol intake, and avoid smoking. Stay informed about the symptoms of breast cancer and perform regular self-examinations. Maintaining a healthy weight and managing stress are also beneficial for overall well-being.]")
    else:
        cont.write("Result: :red[There is a chance of Breast Cancer]")
        cont.write("Recomendation:\n:blue[Given your high risk of breast cancer, it's crucial to schedule an appointment with an oncologist for further evaluation and potential preventive measures. Regular screenings, such as mammograms, and lifestyle modifications, including a healthy diet, regular exercise, limiting alcohol, and avoiding smoking, are essential. Genetic counseling and possible preventive medications or surgeries might also be discussed.]")
