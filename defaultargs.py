from airflow import DAG
from airflow.operators.bash import  BashOperator 
from pendulum import DateTime
from datetime import datetime, timedelta

default_args ={
    'depends_on_past': False,
    'start_date': DateTime(2024,1,23),
    'email': ['test@test.com'],
    'email_on_failure': False,
    'email_on_retry' : False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

dag = DAG('defaultargs', description= "DAG de Exemplo", 
          default_args= default_args,
          schedule_interval='@hourly',
          start_date=datetime(2024,1,15),catchup=False, default_view='graph', 
          tags=['processo', 'tag', 'pipeline'])


task1 = BashOperator(task_id="tsk1",bash_command="sleep 5", dag=dag, retries=3)
task2 = BashOperator(task_id="tsk2",bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tsk3",bash_command="sleep 5", dag=dag)

# Sequencia de execução das tasks

task1 >> task2 >> task3