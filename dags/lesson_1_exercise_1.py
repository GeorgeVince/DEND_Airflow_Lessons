# Instructions
# Define a function that uses the python logger to log a function. Then finish filling in the details of the DAG down below. Once you’ve done that, run "/opt/airflow/start.sh" command to start the web server. Once the Airflow web server is ready,  open the Airflow UI using the "Access Airflow" button. Turn your DAG “On”, and then Run your DAG. If you get stuck, you can take a look at the solution file or the video walkthrough on the next page.

import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


#
# TODO: Define a function for the PythonOperator to call and have it log something
#
def hello_world():
     logging.info("Hello world")

def bye_world():
     logging.info("Bye bye")

dag = DAG(
        'lesson1_exercise1',
        start_date=datetime.datetime.now())


greet_task = PythonOperator(
   task_id="first_dag",
   python_callable=hello_world,
   dag=dag
)

goodbye_task = PythonOperator(
   task_id="second_dag",
   python_callable=bye_world,
   dag=dag
)

greet_task << goodbye_task