# Chicago Crime Rate Prediction using Prophet Model and FastAPI

This repository contains code for predicting the Chicago crime rate using a Prophet model and exposing the functionality through a FastAPI application. Additionally, it demonstrates how to automate tasks using Apache Airflow pipelines.

## Project Overview

- Built a Prophet model to predict the Chicago crime rate based on historical data from 2012 to 2017.
- Developed a FastAPI application that allows users to upload crime data files, train the model, and predict crime rates for a specified number of months.
- Created Airflow pipelines to automate the process of data uploading, model training, and prediction.

## Components

### Prophet Model

The Prophet model is trained on historical crime data from 2012 to 2017. It uses time series forecasting techniques to predict crime rates for future months.

### FastAPI Application

The FastAPI application serves as an interface for users to interact with the Prophet model. It provides the following endpoints:

- **GET /get/:** A simple endpoint to check the availability of the FastAPI application.

- **POST /upload/:** Allows users to upload crime data files. The uploaded data is preprocessed and used to train the Prophet model.

- **POST /predict/:** Accepts the number of months as a parameter and returns the predicted crime rates for the specified number of months.

### Airflow Pipelines

The Airflow pipelines automate the following tasks:

1. **Upload Task:** Uploads the crime data file to the FastAPI application for training.

2. **Prediction Task:** Sends a request to the FastAPI application to predict crime rates for a specified number of months.

## Usage

1. Clone the repository:
  

3. Start the FastAPI application:

4. Access the FastAPI documentation at `http://localhost:8000/docs` to interact with the API endpoints.

5. Set up Airflow and create a DAG using the provided Airflow code. The DAG automates the data upload and prediction tasks.

## Credits

- Built by M Hamza Ghani, Ameer Hamza



