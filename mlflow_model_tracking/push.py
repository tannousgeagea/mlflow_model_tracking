
from core import push, client

model_name = "CraneDetectionBunker"
model_path = "/media/appuser/mlflow/models/CraneDetectionBunker_V11.pt"

metrics = {
    "mAP50": 0.977,
    "mAP50-95": 0.751,
    "precision": 0.954,
    "recall": 0.955,
}

# tags = ["yolo26m", "bunker", "valorsul", "agr", "high_severity_impurity",]

tags = None
push(model_name=model_name, model_path=model_path, metrics=metrics, tags=tags)

# # client.delete_registered_model(name='wasteant-segments')

# yolo_model = ModelWrapper(weights=model_path)
# a=mlflow.pyfunc.log_model(artifact_path="model",
#                             python_model=yolo_model,
#                             artifacts={"weights": model_path},
#                             )

# b=mlflow.register_model(a.model_uri, model_name)

# client = mlflow.MlflowClient()
# client.set_registered_model_alias(b.name,alias,b.version)