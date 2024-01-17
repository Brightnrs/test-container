FROM --platform=linux/amd64 apache/airflow:2.8.0

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN pip install apache-airflow-providers-mongo==3.5.0 \
airflow-provider-great-expectations==0.2.7
