import joblib
import pandas as pd
from e_commerce.entity.config_entity import prediction

class PredictionComponent:
    def __init__(self,config:prediction):
        self.config = config
        self.model = joblib.load(self.config.model_path)
        self.scaler = joblib.load(self.config.scaler_path)
    def predict(self,input:pd.DataFrame):
        scaled_data = self.scaler.transform(input)
        predicted = self.model.predict(scaled_data)

        
        segment_map = {
            0: "Churned / At-Risk Customers",
            1: "High-Value Loyal Customers",
            2: "Potential Loyalists"
        }

        label = segment_map.get(predicted[0],"Unknown")
        return label