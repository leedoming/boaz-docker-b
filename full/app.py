import streamlit as st
import numpy as np

# Streamlit 애플리케이션 시작
st.title('보아즈 로또왕💰')

# 로또 번호 추천 함수
def lotto_numbers():
    return np.random.choice(range(1, 46), size=6, replace=False)

# 추천된 로또 번호 표시
if st.button('로또 번호 추천하기'):
    lotto_numbers = lotto_numbers()
    st.write('추천된 로또 번호:', ', '.join(map(str, sorted(lotto_numbers))))

# 안내 메시지
st.write('Docker 이미지 빌드 실습. 버튼을 클릭해 행운의 로또 번호를 받아보세요🍀')
