import streamlit as st

def session_state_advanced():
    st.title("고급 세션 상태 관리")

    if 'data' not in st.session_state:
        st.session_state.data = []
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
   
    def increment_counter():
        st.session_state.counter += 1
    def add_data():
        if st.session_state.input_value:
            st.session_state.data.append(st.session_state.input_value)
            st.session_state.input_value = ""
    
    st.text_input("데이터 입력", key="input_value", on_change=add_data)
    st.button("카운터 증가", on_click=increment_counter)
    st.write(f"카운터: {st.session_state.counter}")
    st.write("입력된 데이터:", st.session_state.data)

if __name__ == "__main__":
    session_state_advanced()