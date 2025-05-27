import os
from pathlib import Path
import pandas as pd
from e_commerce import logger
from e_commerce.entity.config_entity import PreProcessing




class PreProcessingComponent:
    def __init__(self,config:PreProcessing):
        self.config = config

    def load_data(self):
        if not os.path.exists(self.config.data_path):
            raise FileNotFoundError(f"Input file not found: {self.config.data_path}")
        return pd.read_excel(self.config.data_path)
    def data_cleaning(self):
        df = self.load_data()
        with open(os.path.join(self.config.data_report,'pre_info.txt'),'w') as f:
            f.write(str(df.isna().sum()))
        logger.info(f"check {self.config.data_report} for data reports")
        
        # data cleaning 
        df = df.dropna()
        df = df.dropna(subset=['CustomerID'])
        df = df.drop(['Description','Country'],axis = 1 )
        # Convert CustomerID to string (for grouping)
        df['CustomerID'] = df['CustomerID'].astype(dtype=str)
        df = df.reset_index(drop=True)
        logger.info('data cleaning completed')

        cleaned_file_path = os.path.join(self.config.cleaned_data_save_path,"pre_processed.csv")
        df.to_csv(cleaned_file_path, index=False)
        logger.info(f"Cleaned data saved to: {cleaned_file_path}")
