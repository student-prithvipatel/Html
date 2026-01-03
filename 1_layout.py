import streamlit as st
st.set_page_config(page_title="hello streamlit", page_icon="#",layout="centered")
st.title("Student Infomation")
st.sidebar.header("Profile setting")
student=st.sidebar.text_input("Student Name","prithvi patel")
dept=st.sidebar.selectbox("Department",["ce",'it','cst','csit'])
sem=st.sidebar.slider("Current Semeter",1,8,1)
st.sidebar.markdown("____")
col1,col2=st.columns([1,2])
with col1:
    st.write("Basic Infomation")
    st.write(f"**Name** {student}")
    st.write(f"**Department** {dept}")
    st.write(f"**Semester** {sem}")
with col2:
    st.subheader("About..")
    st.write("....")
with st.expander("subjects"):
    st.write("Ps")
    st.write("Fsd")
    st.write("Python")