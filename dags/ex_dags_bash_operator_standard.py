from airflow import DAG
import datetime
import pendulum
from airflow.operators.empty import EmptyOperator

my_dag = DAG(
    dag_id="dags_bash_operator",
    schedule="0 11 * * 1,5",
    start_date=pendulum.datetime(2024, 6, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["homework"]
)
bash_t1 = EmptyOperator(task_id="bash_t1",
                        dag=my_dag,
                        bash_command="echo whoami",
                        )
bash_t2 = EmptyOperator(task_id="bash_t2",
                        dag=my_dag,
                        bash_command="echo $HOSTNAME",
                        ) 

bash_t1 >> bash_t2