install:
		pip install -r requirements.txt

init_docker_compose:
		mkdir ./logs ./plugins
		echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
		docker-compose up airflow-init
		docker-compose up

run_dag:
		docker-compose run airflow-worker airflow dags trigger my_dag