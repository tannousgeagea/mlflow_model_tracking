# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /mlflow

# Install MLflow and any other necessary dependencies
RUN pip install mlflow psycopg2-binary

# Expose the port that MLflow uses
EXPOSE 5000

# Define the entrypoint to run the MLflow server
ENTRYPOINT ["mlflow", "server"]
