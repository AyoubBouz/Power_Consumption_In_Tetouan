import joblib 
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import  OneHotEncoder




class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_training/model.joblib'))

    
    def predict(self, data):

        prediction = self.model.predict(data)

        return prediction