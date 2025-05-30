import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from e_commerce.entity.config_entity import EDA


class EDAComponent:
    def __init__(self,config : EDA):
        self.config = config

    def load_data(self):
        if not os.path.exists(self.config.data_path):
            raise FileNotFoundError(f"Input file not found: {self.config.data_path}")
        return pd.read_csv(self.config.data_path)

    def get_EDA(self):
        rmf_df = self.load_data()

        rmf = rmf_df[['recency', 'frequency', 'monetary']]

        # Histograms
        plt.figure(figsize=(12,10))
        rmf.hist(bins=10, figsize=(12, 6))
        plt.suptitle('Distributions of Recency, Frequency, and Monetary', fontsize=16)
        plt.savefig(os.path.join(self.config.report,"histograms.png"))
        plt.clf()

        # Boxplots to spot outliers
        plt.figure(figsize=(12, 5))
        for i, col in enumerate(rmf.columns):
            plt.subplot(1, 3, i+1)
            sns.boxplot(y=rmf[col])
            plt.title(f'Boxplot of {col}')
        plt.tight_layout()
        plt.savefig(os.path.join(self.config.report,"boxplots.png"))
        plt.clf()


        # correlation
        plt.figure(figsize=(6,4))
        sns.heatmap(rmf.corr(),annot=True,cmap='coolwarm')
        plt.title('RFM Feature Correlation')
        plt.savefig(os.path.join(self.config.report,"correlation.png"))
        plt.clf()


        # pairplots
        
        sns.pairplot(rmf)
        plt.suptitle('Pairplot of RFM Features', y=1.02)
        plt.savefig(os.path.join(self.config.report,"pairplot.png"))
        plt.clf()
