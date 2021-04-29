"""
File responsible for the implementation of the workflow
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import (
    datetime,
    timedelta
)

from src.preprocessing import (
    preprocess_clinical_trials,
    preprocess_drugs,
    preprocess_pubmed
)
from src.processing import (
    process_clinical_trial,
    process_pubmed
)
from src.output_management import merging


dag = DAG(
    dag_id="my_dag",
    start_date=datetime(2021, 4, 29),
    schedule_interval='@daily',
    catchup=False
)


# Preprocessing steps

drugs_preprocessing = PythonOperator(
    task_id="drugs_preprocessing",
    python_callable=preprocess_drugs.main,
    dag=dag
)

pubmed_preprocessing = PythonOperator(
    task_id="pubmed_preprocessing",
    python_callable=preprocess_pubmed.main,
    dag=dag
)

clinical_trials_preprocessing = PythonOperator(
    task_id="clinical_trials_preprocessing",
    python_callable=preprocess_clinical_trials.main,
    dag=dag
)


# Processing steps

pubmed_processing = PythonOperator(
    task_id="pubmed_processing",
    python_callable=process_pubmed.main,
    dag=dag
)

clinical_trials_processing = PythonOperator(
    task_id="clinical_trials_processing",
    python_callable=process_clinical_trial.main,
    dag=dag
)

# Output manamement step

output_management = PythonOperator(
    task_id="output_management",
    python_callable=merging.main,
    dag=dag
)

# task hierarchy

drugs_preprocessing >> [pubmed_processing, clinical_trials_processing]
pubmed_preprocessing >> pubmed_processing
clinical_trials_preprocessing >> clinical_trials_processing
pubmed_processing >> output_management
clinical_trials_processing >> output_management