import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 
from e_commerce.entity.config_entity import outlier






class OutlierComponent:
    def __init__(self,config:outlier):
        self.config = config
    
    def load_data(self):
        if not os.path.exists(self.config.data_path):
            raise FileNotFoundError(f"Input file not found: {self.config.data_path}")
        return pd.read_csv(self.config.data_path)

    def outlier_removal(self):
        df = self.load_data()
        rmf = df.drop(["CustomerID"],axis=1)
        for col in rmf.columns:
            q1 = rmf[col].quantile(0.25)
            q3 = rmf[col].quantile(0.75)
            IQR = q3-q1
            lower = q1-(1.5*IQR)
            upper = q3+(1.5*IQR)
            rmf = rmf[(rmf[col] >= lower) & (rmf[col] <= upper)]
        rmf.to_csv(os.path.join(self.config.output_path,"rmf_final.csv"),index=False)

        # lets do some eda with this data 
        # EDA - Histogram
        plt.figure(figsize=(12, 10))
        rmf.hist(bins=10, figsize=(12, 6))
        plt.suptitle('Distributions of Recency, Frequency, and Monetary', fontsize=16)
        plt.savefig(os.path.join(self.config.report, "histograms.png"))
        plt.clf()

        # EDA - Boxplots
        plt.figure(figsize=(12, 5))
        for i, col in enumerate(rmf.columns):
            plt.subplot(1, len(rmf.columns), i+1)
            sns.boxplot(y=rmf[col])
            plt.title(f'Boxplot of {col}')
        plt.tight_layout()
        plt.savefig(os.path.join(self.config.report, "boxplots.png"))
        plt.clf()

        # EDA - Correlation Heatmap
        plt.figure(figsize=(6, 4))
        sns.heatmap(rmf.corr(), annot=True, cmap='coolwarm')
        plt.title('RFM Feature Correlation')
        plt.savefig(os.path.join(self.config.report, "correlation.png"))
        plt.clf()

        # EDA - Pairplot
        sns.pairplot(rmf)
        plt.suptitle('Pairplot of RFM Features', y=1.02)
        plt.savefig(os.path.join(self.config.report, "pairplot.png"))
        plt.clf()