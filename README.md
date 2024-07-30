# Power_Consumption_In_Tetouan


import dagshub
dagshub.init(repo_owner='AyoubBouz', repo_name='Power_Consumption_In_Tetouan', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)