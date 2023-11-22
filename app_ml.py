import streamlit as st
import joblib
import numpy as np

def run_ml_app() :
    st.subheader("구매 금액 예측")

    regressor = joblib.load("./model/regressor.pkl")
    
    gender = st.radio("성별 선택", ["남자","여자"])
    st.text(f"성별은 {gender}입니다.")
    # 문자열은 숫자로 처리한다
    if gender == "남자" :
        gender = 1
    else : gender = 0 
    age = st.number_input("나이 입력", 20 , 100)
    st.text(f"나이는 {age}세 입니다.")
    salary = st.number_input("연봉 입력", 20000 , 100000)
    st.text(f"연봉은 {salary}$ 입니다.")
    debt = st.number_input("카드빚 입력", 100 , 20000)
    st.text(f"카드빚은 {debt}$ 입니다.")
    worth = st.number_input("자산 입력", 20000 , 1000000)
    st.text(f"자산은 {worth}$ 입니다.")

    if st.button("구매 예상 금액!") :
        new_data = np.array([gender,age,salary,debt,worth])
        new_data = new_data.reshape(1,5)
        y_pred = regressor.predict(new_data)

        price = int(y_pred[0])
        if price <= 0 :
            st.text("자동차를 구매하기 어렵습니다.")
        elif price > 0 : 
            st.text(f"구매 예상 금액은 : {price}$ 입니다." )
        
    else : st.text("")