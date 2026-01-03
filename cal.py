import streamlit as st
st.title("number input")
a=st.number_input("enter number 1:")
b=st.number_input("enter number 2:")
selected=st.selectbox("instruction",['+','-','*','/'])
if selected=="+":
    st.write("addition=",a+b)
elif selected=="-":
    st.write("substraction=",a-b)
if selected=="*":
    st.write("multiply=",a*b)
if selected=="/":
    st.write("divide=",a/b)