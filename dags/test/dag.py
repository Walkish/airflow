from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from test import app

default_args = {
    "owner": "airflow",
    "start_date": datetime(2022, 12, 6),
    "depends_on_past": False,
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "first_test_dag",
    default_args=default_args,
    description="Very first test dag",
    schedule_interval="*/1 * * * *",
)

s1 = PythonOperator(task_id="first_test_dag", python_callable=app.run, dag=dag)
