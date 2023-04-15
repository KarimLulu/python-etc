ARG AIRFLOW_BASE_IMAGE="apache/airflow:2.0.0-python3.8"
FROM ${AIRFLOW_BASE_IMAGE}

RUN pip install --user --no-cache-dir \
    apache-airflow-providers-cncf-kubernetes==1.0.0
RUN pip uninstall  --yes azure-storage
RUN pip install -U azure-storage-blob apache-airflow-providers-microsoft-azure==1.1.0