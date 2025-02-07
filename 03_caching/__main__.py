import streamlit as st
import pandas as pd
import time
import numpy as np


@st.cache_data
def load_large_dataset():
    """큰 데이터셋 로드 (캐시 사용)"""
    time.sleep(2)  # 데이터 로딩 시뮬레이션
    return pd.DataFrame(
        np.random.randn(1000, 5),
        columns=['A', 'B', 'C', 'D', 'E']
    )


@st.cache_data
def expensive_computation(n):
    """비용이 많이 드는 계산 (캐시 사용)"""
    time.sleep(2)  # 계산 시뮬레이션
    return np.sum([i**2 for i in range(n)])


def caching_demo():
    st.title("Streamlit 캐싱 데모")

    # 데이터셋 로드
    st.header("1. 데이터셋 로드")
    with st.spinner("데이터 로딩 중..."):
        df = load_large_dataset()
    st.dataframe(df, height=200)

    # 계산 실행
    st.header("2. 계산 실행")
    n = st.slider("N 선택", 1, 1000, 100)
    with st.spinner("계산 중..."):
        result = expensive_computation(n)
    st.write(f"결과: {result}")


if __name__ == "__main__":
    caching_demo()cd 