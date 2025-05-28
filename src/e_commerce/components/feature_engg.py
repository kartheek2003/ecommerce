import pandas as pd
import datetime
import os 
from e_commerce.entity.config_entity import FeatureEngineeringconfig


class FeatureEnggComponent:
    def __init__(self,config:FeatureEngineeringconfig):
        self.config = config
    
    def load_data(self):
        if not os.path.exists(self.config.data_path):
            raise FileNotFoundError(f"Input file not found: {self.config.data_path}")
        return pd.read_csv(self.config.data_path)
        

    def feature_engg(self):
        df = self.load_data()
        
        # recency
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
        ref_date = df['InvoiceDate'].max()+datetime.timedelta(days=1)
        df['recency'] = (ref_date - df['InvoiceDate']).dt.days
        recency_df = df.groupby(['CustomerID'])['recency'].min().reset_index()

        # monetary
        df['monetary'] = df['Quantity']*df['UnitPrice']
        monetary_df = df.groupby(['CustomerID'])['monetary'].sum().reset_index()
        monetary_df.columns = ['CustomerID','monetary']

        # frequency
        frequency_df = df.groupby(['CustomerID'])['InvoiceDate'].nunique().reset_index()
        frequency_df.columns = ['CustomerID','frequency']
        

        # rmf_data
        rmf_df = recency_df.merge(frequency_df,on='CustomerID').merge(monetary_df,on='CustomerID')

        rmf_df.to_csv(os.path.join(self.config.output_path,'rmf.csv'))