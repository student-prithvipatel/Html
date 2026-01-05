import streamlit as st
from datetime import date,time
st.title("example for date,time and file upload")
exam_date=st.date_input("select exam date: ", value=date.today())
start_time=st.time_input("Enter exam time: ",value=time(14,0))
file=st.file_uploader("upload ypur pdf file: ",type=['pdf'])
st.write("Exam date and time: ", exam_date,start_time)