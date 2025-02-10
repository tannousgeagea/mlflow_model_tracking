
from core import push, client

model_name = "iserlohn.amk.front.want:waste.impurity"
model_path = "/media/appuser/mlflow/amk.front.impurity.v7.pt"

metrics = {
    "mAP50": 0.66,
    "mAP50-95": 0.45,
    "precision": 0.755,
    "recall": 0.592,
}

push(model_name=model_name, model_path=model_path, metrics=metrics)

# # client.delete_registered_model(name='wasteant-segments')

# yolo_model = ModelWrapper(weights=model_path)
# a=mlflow.pyfunc.log_model(artifact_path="model",
#                             python_model=yolo_model,
#                             artifacts={"weights": model_path},
#                             )

# b=mlflow.register_model(a.model_uri, model_name)

# client = mlflow.MlflowClient()
# client.set_registered_model_alias(b.name,alias,b.version)