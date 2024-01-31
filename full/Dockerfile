# 베이스 이미지 선택 - python:3.8
FROM python:3.8

WORKDIR /app

# 필요한 패키지 설치
RUN pip install --upgrade pip \
    && pip install streamlit numpy

# 애플리케이션 설정 - 소스 코드 복사
COPY app.py /app/app.py

# 노출할 포트 지정- streamlit 포트 8501
EXPOSE 8501

# 애플리케이션 실행
CMD ["streamlit", "run", "app.py"]
