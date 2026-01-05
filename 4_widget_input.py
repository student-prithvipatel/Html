import streamlit as st
course=st.selectbox("select course",["python",'fsd','ps','de'])
day=st.multiselect('prefered day for extra lecture',['mon','tue','wed','thu','fri','sat'])
lect_no=st.radio("prefered lect no:",[1,2,3,4])
st.write(f"prefered days: {",".join(day) if day else "None"}")
st.write("course : ",course)
st.write("lec no : ",lect_no)

