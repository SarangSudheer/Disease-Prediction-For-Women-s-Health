import streamlit as st

def page():
    
    set1,set2=st.columns([0.7,0.3])
    with set1:
        st.title("_Calorie Intake Calculator_")
    with set2:
        st.image("icon/calories-calculator.png",width=100)
    st.subheader("Please type in the below values: ")

    with st.form("_form"):
        weight=st.number_input("Body Weight (in Kg)")
        height=st.number_input("Height (in cm)")
        age=st.number_input("Age")
        submit=st.form_submit_button("Calculate")
        opt=st.radio("**Activity Level**",
                          ["Sedentary","Lightly active","Moderately active","Very active","Super active"],
                          captions=["little or no exercise",
                                    "light exercise/sports 1-3 days/week",
                                    "moderate exercise/sports 3-5 days/week",
                                    "hard exercise/sports 6-7 days a week",
                                    "very hard exercise/physical job & exercise 2x/day"]
                                    )
        act_dict={"Sedentary":1.2,"Lightly active":1.375,"Moderately active":1.55,"Very active":1.725,"Super active":1.9}
        act_lvl=act_dict[opt]
    if submit:
      calc(weight,height,age,act_lvl)

def calc(weight,height,age,act_lvl):
      BMR=655+(9.6*weight)+(1.8*height)-(4.7*age)
      calories=BMR*act_lvl
      cont=st.container(border=True)
      cont.write(f"You should take in about _:orange[**{calories:.2f}**]_ of calories per day.")