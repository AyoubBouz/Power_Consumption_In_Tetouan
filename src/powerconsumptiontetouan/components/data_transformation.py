import os
from powerconsumptiontetouan import logger
from powerconsumptiontetouan.entity.config_entity import DataTransformationConfig

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config



    def preprocessing_features_data(self):
        data = pd.read_csv(self.config.data_path)
        data.Datetime = pd.to_datetime(data.Datetime)
        data['month'] = data.Datetime.dt.month
        data['weekday'] = data.Datetime.dt.day
        data['time'] = data.Datetime.dt.time.astype(str)
        features = ['Temperature', 'Humidity', 'WindSpeed', 'GeneralDiffuseFlows', 'DiffuseFlows',  'month', 'weekday', 'time']
        targets = ['PowerConsumption_Zone1','PowerConsumption_Zone2', 'PowerConsumption_Zone3']
        data_features =data[features]
        numerical_features = data_features.drop(columns=['time']).columns
        time_feature = ['time']
        scaler = MinMaxScaler()
        data_features[numerical_features] = scaler.fit_transform(data_features[numerical_features])
        encoder = OneHotEncoder(handle_unknown="ignore")
        # OneHot encode the 'time' feature
        time_encoded = encoder.fit_transform(data_features[time_feature])

        time_encoded_df = pd.DataFrame(time_encoded.todense())
        # Concatenate the encoded time values with the scaled DataFrame

        data_features = pd.concat([data_features, time_encoded_df], axis=1)

        # Drop the original 'time' and 'time_seconds' columns
        data_features = data_features.drop(columns=['time'])

        data_targets=data[targets]

        data_ml=pd.concat([data_features,data_targets],axis=1)

        train, test = train_test_split(data_ml,test_size=0.33)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)


    
    


