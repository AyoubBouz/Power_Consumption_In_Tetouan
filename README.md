# Power_Consumption_In_Tetouan

## Overview

The **Power_Consumption_In_Tetouan** project aims to predict power consumption in the city of Tetouan, Morocco, using machine learning techniques. The project involves data preprocessing, feature engineering, model training, and evaluation. Additionally, MLflow is used for experiment tracking, and the final model is deployed on AWS for scalable and accessible predictions.

## Table of Contents
- [Installation](#installation)
- [Data](#data)
- [Preprocessing & Feature Engineering](#preprocessing-feature-engineering)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [MLflow Integration](#mlflow-integration)
- [AWS Deployment](#aws-deployment)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AyoubBouz/Power_Consumption_In_Tetouan.git
    cd Power_Consumption_In_Tetouan
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Data

The dataset used in this project contains power consumption data for Tetouan in 2017.

## Preprocessing & Feature Engineering

Data preprocessing steps are implemented in `data_transformation.py` and the corresponding Jupyter notebook `data_transformation_notebook.ipynb`. The preprocessing steps include handling missing values, scaling, and encoding categorical variables.

## Model Training

The model training process involves training several machine learning models (ElasticNet, RandomForest, GradientBoosting) and selecting the best one based on performance metrics. This is handled in `model_trainer.py` and `model_trainer.ipynb`. MLflow is used to track the experiments and log the results.

## Model Evaluation

Model evaluation is conducted to assess the performance of the trained models. The evaluation metrics (RSME, MAE, R2) and results are documented in `model_evaluation.py` and `model_evaluation.ipynb`.

## MLflow Integration

MLflow is integrated into the project to track experiments, log metrics, and store models. The `mlruns/` directory contains the logged experiments.

## AWS Deployment

Using Github Actions, EC2 & ECR.

## UI

UI interface using Flask and HTML (bootstrap) for training and testing the model.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to reach out if you have any questions or need further assistance. Happy coding!