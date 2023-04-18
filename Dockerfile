FROM apache/airflow:2.5.1

ENV AIRFLOW_HOME=/opt/airflow

WORKDIR $AIRFLOW_HOME

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip

COPY scripts scripts

USER $AIRFLOW_UID

RUN python3 -m pip install --no-cache-dir -r requirements.txt