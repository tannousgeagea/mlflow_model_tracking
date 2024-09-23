
from core import push, client

model_name = "iserlohn.amk.want:waste.impurity"
model_path = "/media/appuser/mlflow/base.impurity.pt"

push(model_name=model_name, model_path=model_path)

# # client.delete_registered_model(name='wasteant-segments')

# yolo_model = ModelWrapper(weights=model_path)
# a=mlflow.pyfunc.log_model(artifact_path="model",
#                             python_model=yolo_model,
#                             artifacts={"weights": model_path},
#                             )

# b=mlflow.register_model(a.model_uri, model_name)

# client = mlflow.MlflowClient()
# client.set_registered_model_alias(b.name,alias,b.version)