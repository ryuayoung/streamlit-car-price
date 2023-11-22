import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda_app() :
    st.subheader("데이터 분석")

    st.text("전체 데이터 프레임 확인하기")

    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    st.dataframe(df)

    st.text("기초통계데이터 확인하기")
    
    if st.checkbox("통계데이터 보기") : 
        st.dataframe(df.describe())
    else : st.text("")    

    st.text("최대 / 최소 데이터 확인하기")
    column_list = df.columns[ 4 : ]
    
    selected_column = st.selectbox("컬럼을 선택하세요" , column_list)
    st.text(f"{selected_column} 컬럼의 최소값")
    st.dataframe(df.loc[ df[selected_column] == df[selected_column].min()])
    
    st.text(f"{selected_column} 컬럼의 최대값")
    st.dataframe(df.loc[ df[selected_column] == df[selected_column].max()])

    st.text(f"{selected_column} 컬럼의 히스토그램")
    fig1 = plt.figure()
    df[selected_column].hist(bins = 20)
    st.pyplot(fig1)
