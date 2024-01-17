from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from airflow.utils import timezone

# use requests to get json data from API
def _extract():
    import requests
    import pandas as pd

    url='https://api-v3.thaiwater.net/api/v1/thaiwater30/api_service?mid=74&eid=lFVf39F_K1BPDFGvt7IBtDOpApT--85ckAhioL_PxmaUl79Z8jcvhjTpz592A53BORAhEvK8RoEZK8i1cq3COg'
    r=requests.get(url)
    df=pd.DataFrame(r.json())
    return df


# Function to import the DataFrame into PostgreSQL
def _load_data_into_database(**context):
    import psycopg2
    import pandas as pd
    from sqlalchemy import create_engine

    # create connection and engine
    db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "postgres",
    "port": "5432"
    }

    try:
        # Create a connection to the PostgreSQL database
        conn = psycopg2.connect(**db_params)

        # Create an SQLAlchemy engine for data ingestion
        engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')

        # Retrieve the DataFrame from Airflow XComs
        data = context["ti"].xcom_pull(task_ids="extract", key="return_value")
        df = pd.DataFrame(data)

        # Write the DataFrame to the database
        table_name = "dam_daily_egat"  
        df.to_sql(table_name, engine, if_exists='replace', index=False)

        print("Data loaded into PostgreSQL successfully.")
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
    except Exception as e:
        print("Error loading data into PostgreSQL:", e)
    finally:
        if conn:
            conn.close()


default_args = {
    "owner": "bright",
    "start_date": timezone.datetime(2024, 1, 15),
}
with DAG(
    "Dam_Daily_EGAT_def",
    default_args=default_args,
    schedule_interval="@daily",
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=_extract,
    )

    create_import_table = PostgresOperator(
    task_id="create_import_table",
    postgres_conn_id="postgres",
    sql="""
        CREATE TABLE IF NOT EXISTS dam_daily_egat_def (
            dam_date varchar(255),
            dam_evap varchar(255),
            dam_id varchar(255),
            dam_inflow varchar(255),
            dam_level varchar(255),
            dam_losses varchar(255),
            dam_released varchar(255),
            dam_spilled varchar(255),
            dam_storage varchar(255)
            
        )
    """,
    )

    load_data_into_database = PythonOperator(
        task_id="load_data_into_database",
        python_callable=_load_data_into_database,
    )

    extract  >> create_import_table >> load_data_into_database
