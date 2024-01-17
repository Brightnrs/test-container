from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from airflow.utils import timezone
from function import *


default_args = {
    "owner": "bright",
    "start_date": timezone.datetime(2023, 12, 1),
}
with DAG(
    "Dam_Daily_EGAT_def_main",
    default_args=default_args,
    schedule_interval="@daily",
) as dag:

    create_import_table = PostgresOperator(
    task_id="create_import_table",
    postgres_conn_id="postgres",
    sql="""
        CREATE TABLE IF NOT EXISTS dam_daily_egat_main (
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
        python_callable=main,
    )

    create_import_table >> load_data_into_database
