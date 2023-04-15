from datetime import timedelta

import pendulum
import os
from pathlib import Path
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def _calculate_mean(input_file, output_file):
    total, count = 0, 0
    with open(input_file) as f:
        for line in f:
            total += float(line.strip())
            count += 1
    with open(output_file, "w") as f:
        f.write(str(total / count))


data_path = Path(os.path.dirname(os.path.abspath(__file__)))
input_file = data_path / "data.txt"
output_file = data_path / "statistics.txt"

dag = DAG(
    dag_id="process_data",
    start_date=pendulum.now('UTC'),
    schedule_interval=timedelta(seconds=15)
)

get_data = BashOperator(
    task_id="get_data",
    bash_command=f"echo '101.5\n45.7' > {input_file}",
)
get_mean = PythonOperator(
    task_id="calculate_mean",
    python_callable=_calculate_mean,
    op_kwargs={"input_file": input_file, "output_file": output_file},
    dag=dag,
)
generate_report = BashOperator(
    task_id="generate_report",
    bash_command=f"cat {output_file}",
)

cleanup_files = BashOperator(
    task_id="cleanup_resources",
    bash_command=f"rm {input_file} & rm {output_file}",
    trigger_rule="all_done"
)

echo = BashOperator(
    task_id="echo",
    bash_command="echo 123",
    trigger_rule="all_done"
)

get_data >> get_mean >> generate_report >> cleanup_files >> echo
