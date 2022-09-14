from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import logging
import pandas as pd
import requests

import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

with DAG(
    dag_id='wcbrr',
    schedule_interval='0 7 * * 6',
    start_date=datetime(year=2022, month=9, day=13),
    catchup=False
) as dag:
    pass