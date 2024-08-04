import streamlit as st

def page():
    
    set1,set2=st.columns([0.7,0.3])
    with set1:
        st.title("_Water Intake Calculator_")
    with set2:
        st.image("icon/water-bottle.png",width=100)
    st.subheader("Please type in the below values: ")

    with st.form("_form"):
        weight=st.number_input("Body Weight (in Kg)")
        submit=st.form_submit_button("Calculate")
    if submit:
      calc(weight)

def calc(weight):
      water=(weight*35)/1000
      cont=st.container(border=True)
      cont.write(f"You should drink about _:blue[**{water:.2f}**]_ liters of water per day.")