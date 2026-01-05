import streamlit as st
import pandas as pd
from datetime import date,time
st.set_page_config(page_title="Student marks and feedback from: ", page_icon="📃",layout="centered")
st.title("Student marks and feedback from")
st.header("1. Student information")
col1,col2=st.columns([1,2])
with col1:
    en_no=st.text_input("Enrollment number")
    name=st.text_input("Enter name")
with col2:
    sem=st.selectbox("semeter",[1,2,3,4,5,6,7,8])
    div=st.text_input("division","CSE(CS)-D3")
exam_time=st.date_input("select exam date: ", value=date.today())
st.header("2. marks entry")
py1=st.number_input("python1 marks(out of 100) : ",min_value=0,max_value=100,value=0)
ps=st.number_input("ps marks(out of 100) : ",min_value=0,max_value=100,value=0)
fsd=st.number_input("fsd marks(out of 100) : ",min_value=0,max_value=100,value=0)
de=st.number_input("de marks(out of 100) : ",min_value=0,max_value=100,value=0)

st.header(" 3. feedback ")
understanding= st.slider("how well did ypu understand the subject",1,10,10)
participation=st.radio("class participation ",['low','medium','high'])
comment=st.text_area("additional comment")
if st.button("submit record"):
    if not en_no or not name:
        st.error("please fill enrollment nuber and name")
    else:
        df=pd.DataFrame({"Enrollment_No":[en_no],
                         "Name":[name],
                         "Semester":[sem],
                         "Division":[div],
                         "exam date":[exam_time],
                         "python1":[py1],
                         "ps":[ps],
                         "fsd":[fsd],
                         "de":[de],
                         "Understanding":[understanding],
                         "Participation":[participation],
                         "comment":[comment]
                         })
        st.success("record submitted successfully")
        st.subheader("Preview submitted data")
        st.dataframe(df)
        csv=df.to_csv(index=False,encoding="utf-8")
        st.download_button(label="download from here",
                           data=csv,file_name=f"{en_no}_record.csv",mime="text/csv")
