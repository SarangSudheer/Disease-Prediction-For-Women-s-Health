import streamlit as st
from streamlit_option_menu import option_menu
import Breast_Cancer,Heart_Failure,Diabeties,Water_Intake,Caloric_Intake

st.title("Disease Prediction and Health Recomendation System")
with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options=["Diabetes","Heart Failure","Breast Cancer","Water Intake","Calorie Intake"],
        menu_icon="cast",
    )


if selected == "Diabetes":
    Diabeties.page()
if selected == "Heart Failure":
    Heart_Failure.page()
if selected=="Breast Cancer":
    Breast_Cancer.page()
if selected=="Water Intake":
    water_intake.page()
if selected=="Calorie Intake":
    caloric_intake.page()
