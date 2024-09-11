import mlflow
from core import pull


model_path = pull(model_name='wasteant.segments.gml')

print(model_path)

model = mlflow.pyfunc.load_model(model_path)

input_image = 'image.jpg'
results = model.predict(input_image)