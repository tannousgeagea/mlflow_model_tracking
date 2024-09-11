import os
import mlflow
from ultralytics import YOLO
from mlflow.tracking import MlflowClient
from utils import print_model_info, print_model_version_info

# Initialize the MLflow Client
mlflow.set_tracking_uri(f"{os.getenv('MLFLOW_TRACKING_URI')}")
client = MlflowClient()

ALIAS_PROD = 'production'

class ModelWrapper(mlflow.pyfunc.PythonModel):
    def __init__(self, weights):
        self.weights = weights

    def load_context(self, context):
        # Load the YOLO model
        self.model = YOLO(self.weights)
        
    def predict(self, context, model_input:str, conf:float=0.25):
        results = self.model.predict(model_input, conf=conf)
        return results
    
    def track(self, context, model_input:str, conf:float=0.25):
        results = self.model.track(model_input, persist=True, conf=conf)
        return results
    
    
def push(model_name, model_path):
    # Start an MLflow run
    with mlflow.start_run() as run:
        yolo_model = ModelWrapper(weights=model_path)
        
        mlflow.pyfunc.log_model(
            artifact_path="model",
            python_model=yolo_model,
            conda_env={
                'name': 'mlflow-env',
                'channels': ['defaults', 'conda-forge'],
                'dependencies': [
                    'python=3.8',
                    'pip',
                    {
                        'pip': [
                            'mlflow',
                            'torch',
                            'ultralytics',
                        ],
                    },
                ],
            },
        )
        
        # Optionally, log other parameters and metrics
        mlflow.log_param("model_type", "YOLOv8")
        mlflow.log_metric("mAP50", 0.85)

    result = mlflow.register_model(
        model_uri=f"runs:/{run.info.run_id}/model",
        name=model_name
    )
    
    new_version = result.version
    client.set_registered_model_alias(
        name=model_name,
        alias=ALIAS_PROD,
        version=new_version
    )
        
    model = client.get_registered_model(model_name)
    print_model_info(model)

    model = client.get_model_version_by_alias(model_name, alias=ALIAS_PROD)
    print_model_version_info(model)
    
    artifact_uri = client.get_model_version_download_uri(model_name, model.version)
    print(f"Download URI: {artifact_uri}")
    
def pull(model_name, run_id:str=None):
    if run_id:
        model_uri = f'runs:/{run_id}/model'
    else:
        model_version = client.get_model_version_by_alias(model_name, alias=ALIAS_PROD)
        model_uri = model_uri = f"models:/{model_name}/{model_version.version}"
        
    print(f"MODEL_URI: {model_uri}")
    
    local_dir = "/tmp/artifact_downloads"
    if not os.path.exists(local_dir):
        os.mkdir(local_dir)
        
    local_path = mlflow.artifacts.download_artifacts(artifact_uri=model_uri, dst_path=local_dir)
    print(f"LOCAL PATH: {local_path}")
    return local_path
