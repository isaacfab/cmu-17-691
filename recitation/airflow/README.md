# Recitation Outline for Data Pipeline Management using Airflow

> [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html) is an open-source platform for developing, scheduling, and monitoring batch-oriented workflows. Airflow’s extensible Python framework enables you to build workflows connecting with virtually any technology. A web interface helps manage the state of your workflows. Airflow is deployable in many ways, varying from a single process on your laptop to a distributed setup to support even the biggest workflows.

From last week we saw that containers could be used to package application services including machine learning components. This week we talk about how containers can be used together or 'orchestrated' to create more complicated products. This week we look at using `docker-compose` to create a fully working **Airflow** instance which is useful for managing data pipelines.

## example code

Make sure the docker engine is installed. On the command line move to the directory you want to be used for persistence. Remember that containers are ephemeral unless persistent volumes are mounted. Once in the directory you want to use download the `docker-compose.yaml` file:

```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.2/docker-compose.yaml'
```

For Linux give the user the right privileges and create directories used by Airflow

```
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

Initialize the database

```
docker compose up airflow-init
```

Build and run the application

```
docker compose up
```

now the airflow UI can be accessed at `http://localhost:8080` with both username and password `airflow.` Also you can open the jupyter lab instance at `http://localhost:8888` you can get the token from the console startup logs.


When you are done with the Airflow experiment you can clean everything up with

```
docker compose down --volumes --rmi all
```


[Airflow docker documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)