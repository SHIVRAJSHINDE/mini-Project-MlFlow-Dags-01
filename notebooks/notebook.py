import mlflow
import dagshub

dagshubUri = "https://dagshub.com/SHIVRAJSHINDE/mini-Project-MlFlow-Dags-01.mlflow"
mlflow.set_tracking_uri(dagshubUri)

import dagshub
dagshub.init(repo_owner='SHIVRAJSHINDE', repo_name='mini-Project-MlFlow-Dags-01', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


