from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils import timezone
import requests
import pandas as pd
from CREATE_FUNCTION import *
from DB_VARIABLE import *
import logging

# use requests to get json data from API
def _extract():

    url='https://api-v3.thaiwater.net/api/v1/thaiwater30/api_service?mid=74&eid=lFVf39F_K1BPDFGvt7IBtDOpApT--85ckAhioL_PxmaUl79Z8jcvhjTpz592A53BORAhEvK8RoEZK8i1cq3COg'
    r=requests.get(url)
    df=pd.DataFrame(r.json())
    return df

# Function to import the DataFrame into PostgreSQL
def _load_data_into_database(**context):

    # Retrieve the DataFrame from Airflow XComs
    data = context["ti"].xcom_pull(task_ids="extract", key="return_value")
    df = pd.DataFrame(data)
    logging.info("Retrieve data successfully!")

    # Connect Database
    connect_database()
    logging.info("Connect database successfully!")

    # Add timestamp to dataframe
    df = add_timestamp(df)
    logging.info("Add timestamp successfully!")

    # Create or insert table from dataframe
    create_or_insert(dataframe=df, table_info=DTYPE_DICT['Dam_Daily_EGAT'], schema='testing')
    logging.info("Insert table successfully!")

default_args = {
    "owner": "bright",
    "start_date": timezone.datetime(2023, 12, 1),
}
with DAG(
    "Dam_Daily_EGAT_test",
    default_args=default_args,
    schedule_interval="@daily",
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=_extract,
    )


    load_data_into_database = PythonOperator(
        task_id="load_data_into_database",
        python_callable=_load_data_into_database,
    )


    extract >> load_data_into_database
