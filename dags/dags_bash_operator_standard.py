from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="dags_bash_operator_standard",
    schedule="0 11 * * 1,5",
    start_date=pendulum.datetime(2024, 6, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["homework"]
)
bash_t1 = BashOperator(
    task_id="bash_t1",
    dag=dag,
    bash_command="echo whoami"
)
bash_t2 = BashOperator(
    task_id="bash_t2",
    dag=dag,
    bash_command="echo $HOSTNAME"
) 

bash_t1 >> bash_t2