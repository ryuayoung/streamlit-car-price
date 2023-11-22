import streamlit as st

def run_home_app() :
    st.subheader("Welcome ~~")
    st.text("이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.")
    st.text("고객 정보를 넣으면, 차 구매 금액도 예측해 줍니다.")

    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsd9Mv8rBwzy9JSCJZQOalDCipiaUYnfRteA&usqp=CAU", use_column_width=True)