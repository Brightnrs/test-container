import requests
import pandas as pd
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def main():
    #extract
    url='https://api-v3.thaiwater.net/api/v1/thaiwater30/api_service?mid=74&eid=lFVf39F_K1BPDFGvt7IBtDOpApT--85ckAhioL_PxmaUl79Z8jcvhjTpz592A53BORAhEvK8RoEZK8i1cq3COg'
    r=requests.get(url)
    df=pd.DataFrame(r.json())

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