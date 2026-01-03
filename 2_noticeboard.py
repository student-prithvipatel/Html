import streamlit as st
from datetime import date
st.set_page_config(page_title="hello noticeboard", page_icon="$",layout="wide")
st.title("Notice Board")
st.sidebar.header("Filter notices")
selected=st.sidebar.selectbox("Notice category",['all','exam','workshop','intership','general'])
show_past=st.sidebar.checkbox("Show Past Notice",value=True)
notices=[
    {"Title":"T4 Exam","Catagory":"Exam","Date":date(2026,2,1)},
    {"Title":"Python Workshop","Catagory":"workshop","Date":date(2026,2,11)},
    {"Title":"interview","Catagory":"intership","Date":date(2026,4,1)},
    {"Title":"PTM","Catagory":"general","Date":date(2026,12,1)}
]
st.subheader("Notices")
col1,col2=st.columns([1,2])
with col1:
    st.subheader("Filter applied")
    st.write(f"category: **{selected}**")
    st.write("Include past notice:",show_past)
with col2:
    st.subheader("Information")
    st.text("below are filtered notice")
for i in notices:
    if selected!='all' and i["category"]!=selected:
        continue
    with st.expander(f"{i["Title"]} {((i["Catagory"]))}"):
        st.write("data",i["Date"])
        st.write("notice details....")