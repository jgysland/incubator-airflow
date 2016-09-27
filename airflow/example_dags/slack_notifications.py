from airflow.models import DAG
from airflow.operators import PythonOperator
from airflow.exceptions import AirflowException
from datetime import datetime, timedelta

start_time = datetime.combine(datetime.now() - timedelta(minutes=10),
                              datetime.min.time())

args = dict(
    owner='slack-test',
    start_date=start_time,
    retries=3,
    slack_username='airflow-bot',
    slack_channel='@jgys',
    slack_icon_emoji=':airflow:'
    )


def fail():
    raise AirflowException('Testing Slack notifications!')

with DAG(dag_id="slack_notification_test", default_args=args,
         schedule_interval='*/1 * * * *') as dag:
    op = PythonOperator(task_id='failing_task', default_args=args,
                        python_callable=fail)
