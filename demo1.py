import streamlit as st
st.set_page_config(page_title="hello streamlit", page_icon="#",layout="centered")
st.title("Welcome to streamlit")
st.header("This is streamlit")
st.subheader("This is subheader")
st.text("This is _st.text()_")
st.write("This is **_st.write()_**")
st.markdown("This is _Markdown_")
code="""
def add(a,b):
    return a+b
res=add(3,5)
print(res)
"""
st.code(code,language="python")
st.code(code,language="C")
