FROM python:3.13.3-alpine3.21
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

# 设置环境变量
ENV IEXEC_INPUT_FILES_FOLDER=/iexec_in

ENTRYPOINT ["python3", "/app/src/app.py"]
