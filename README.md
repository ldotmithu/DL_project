# DL_project

import dagshub
dagshub.init(repo_owner='ldotmithu', repo_name='DL_project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/ldotmithu/DL_project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="ldotmithu"
os.environ["MLFLOW_TRACKING_PASSWORD"]=""


https://dagshub.com/ldotmithu/DL_project.mlflow