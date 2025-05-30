
from core import push, client

model_name = "WasteTruckParts_agr_V1"
model_path = "/media/appuser/mlflow/TruckGate_agr_V1.pt"

metrics = {
    "mAP50": 0.926,
    "mAP50-95": 0.712,
    "precision": 0.97,
    "recall": 0.7,
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