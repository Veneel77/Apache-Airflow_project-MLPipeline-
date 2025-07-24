from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

## Define our first task
def preprocess_data():
    print("preprocessing data..")

##define task 2
def train_model():
    print("Training model.....")

##define task 3
def evaluate_model():
    print("Evaluate Models....")

##Define the DAG

with DAG(
    'ml_pipeline',
    start_date=datetime(2025,1,1),
    schedule='@weekly'

) as dag:
    

    ##define task
    preprocess=PythonOperator(task_id="preprocess_task" ,python_callable=preprocess_data)
    train=PythonOperator(task_id="train_task",python_callable=train_model)
    evaluate=PythonOperator(task_id="evaluate_task",python_callable=evaluate_model)

    ##set dependencies

    preprocess >> train >> evaluate