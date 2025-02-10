import mlflow
from core import pull


model = pull(model_name='iserlohn.amk.front.want:waste.impurity')

input_image = 'image2.jpg'
results = model.predict(input_image)
unwrapped_model = model.unwrap_python_model()
results = unwrapped_model.track(input_image)