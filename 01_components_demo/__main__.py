import streamlit as st
import time
import numpy as np

def components_demo():
    
    st.title("혜교 컴포넌트 데모")
    st.write("title")
    
    st.header("1. 기본 컴포넌트")
    st.write("header") 

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)
    st.write("progress")

    with st.spinner("처리 중... "):
        time.sleep(2)
    st.success("완료!")

    st.sidebar.header("사이더바 설정")
    name = st.sidebar.text_input("이름")
    age = st.sidebar.slider("나이", 0, 100, 25)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Column 1")
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
    with col2:
        st.header("Column 2")
        st.button("Click me!")
    # with col3:
    #     st.header("Column 3")
    #     st.write("Some text")
    
    # tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
    # with tab1:
    #     st.write("This is tab 1")
    # with tab2:





if __name__ == "__main__":
    components_demo()