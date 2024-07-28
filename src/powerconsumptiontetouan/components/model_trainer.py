import pandas as pd
import os
from powerconsumptiontetouan import logger
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import joblib
from powerconsumptiontetouan.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        features_data = pd.read_csv(self.config.features_data_path)
        targets_data = pd.read_csv(self.config.targets_data_path)

        # zone_1 = targets_data.columns[0]
        # zone_2 = targets_data.columns[1]
        # zone_3 = targets_data.columns[2]

        X_train, X_test, y_train, y_test = train_test_split(features_data, targets_data[self.config.target_column],
                                                                                                   test_size = 0.30,
                                                                                                   random_state = 0)

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(X_train, y_train)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))

