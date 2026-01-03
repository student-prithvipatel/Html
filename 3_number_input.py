import streamlit as st
st.title("number input")
age=st.number_input("enter age:",min_value=0,max_value=80,value=25)
rating=st.slider("give rating",min_value=0,max_value=10,value=2)
st.write("age=",age)
st.write("rating=",rating)