FROM python:latest

RUN apt-get update -y && apt-get upgrade -y

RUN pip3 install -U pip

COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt

RUN pip install flask google-generativeai python-dotenv



CMD python3 -m ChatBot 