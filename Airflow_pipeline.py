

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import requests 
from datetime import datetime, timedelta
from Upload_Operator import HttpFileUploadOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.providers.http.sensors.http import HttpSensor
import json



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['hamza91ghani@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}


dag = DAG(
    'currency_forecast_dag',
    default_args=default_args,
    start_date=datetime(2023, 8, 19),
    description='A DAG to forecast monthly chichgago crime rate',
    schedule=timedelta(days=1),
)



# task=HttpSensor(
# task_id="CheckingConnection",
# http_conn_id="fast_api",
# endpoint='get/',
# dag=dag

# )


Task1 = HttpFileUploadOperator(
    
    endpoint='http://localhost:8000/upload/',
    file_path='/mnt/d/Downloads/ML Projects/P74-Project-3/Project 3/Chicago_Crimes_2012_to_2017.csv',
    dag=dag,
    task_id="Upload_Endpoint"
)


Task2 = SimpleHttpOperator(
    http_conn_id='fast_api',
    endpoint='predict/?months=12',
    method='POST',
    data=json.dumps({}),  # Set an empty JSON object in the data field
    headers={"Content-Type": "application/json"},
    response_check=lambda response: True if response.status_code == 200 else False,
    dag=dag,
    task_id="Predict",
    params={"months": 12}  # Pass the "months" parameter in the query string
)



Task1 >> Task2





