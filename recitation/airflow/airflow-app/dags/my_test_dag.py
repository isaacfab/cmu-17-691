from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from pip import _internal
import requests

args = {
 
    'owner': 'pipis',
    'start_date': days_ago(1)
}
 
dag = DAG(dag_id = 'my_sample_dag', 
    default_args=args, 
    schedule_interval=None)
 
 
def run_this_func():
    print('I am coming first')    
    #print(requests.get("https://catfact.ninja/fact").json())
    print(_internal.main(['list']))
 
def run_also_this_func():
    print('I am coming last')
    #print(requests.get("http://time.jsontest.com/").json())


 
with dag:
    run_this_task = PythonOperator(
        task_id='run_this_first',
        python_callable = run_this_func
    )
 
    run_this_task_too = PythonOperator(
        task_id='run_this_last',
        python_callable = run_also_this_func
    )
 
    run_this_task >> run_this_task_too