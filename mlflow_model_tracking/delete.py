from core import client

# model_name = "iserlohn.amk.want:waste.impurity"
# client.delete_registered_model(name=model_name)

client.delete_model_version(
    name="GasCanisterDet",
    version=4
)