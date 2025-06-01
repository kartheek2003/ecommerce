import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from sklearn.cluster import KMeans
from kneed import KneeLocator
from e_commerce.entity.config_entity import model
import os 

class ModelBuildingComponent:
    def __init__(self,config:model):
        self.config = config
    
    def load_data(self):
        if not os.path.exists(self.config.data_path):
            raise FileNotFoundError(f"file not found at {self.config.data_path}")
        return pd.read_csv(self.config.data_path)
    

    def build_model(self):
        rmf_scaled = self.load_data()
        # model building
        kl = joblib.load(self.config.kl_path)

        km_model = KMeans(n_clusters=kl.elbow,random_state=self.config.random_state)
        joblib.dump(km_model,os.path.join(self.config.models,'km_model.pkl'))

        y_predicted = km_model.fit_predict(rmf_scaled)

        rmf_scaled['cluster'] = y_predicted

        final_op_rmf = rmf_scaled

        

        # segmentation graphs

        

        plt.figure(figsize=(10,6))
        sns.scatterplot(
            x=final_op_rmf['recency'], 
            y=final_op_rmf['monetary'], 
            hue=final_op_rmf['cluster'], 
            palette='viridis',
            alpha=0.7
        )
        plt.title('Customer Segments by Recency and Monetary Value')
        plt.xlabel('Recency (days)')
        plt.ylabel('Monetary Value')
        plt.legend(title='Cluster')
        plt.savefig(os.path.join(self.config.report,'segmentaion.png'))
        plt.clf()

        # pairplots
        sns.pairplot(final_op_rmf, vars=['recency', 'frequency', 'monetary'], hue='cluster', palette='viridis')
        plt.savefig(os.path.join(self.config.report,'pairplot.png'))
        plt.clf()

        # Compute the average RFM values for each cluster
        cluster_profile = final_op_rmf.groupby('cluster')[['recency', 'frequency', 'monetary']].mean().round(1)
        with open("cluster_profile_report.txt", "w") as f:
            f.write("Cluster Profile Report (Mean RFM Values):\n\n")
            f.write(cluster_profile.to_string())

        segment_map = {
            0: 'Loyal Customers',
            1: 'Churned Customers',
            2: 'Potential Loyalists'
        }

        final_op_rmf['segment'] = final_op_rmf['cluster'].map(segment_map)
        final_op_rmf.to_csv(os.path.join(self.config.models, "segmentation_output.csv"), index=False)


        # cluster with segmentation
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            data=final_op_rmf, 
            x='recency', 
            y='monetary', 
            hue='segment', 
            palette='Set1', 
            s=100
        )

        plt.title("Customer Segments based on Recency and Monetary")
        plt.xlabel("Recency (days since last purchase)")
        plt.ylabel("Monetary (total spending)")
        plt.legend(title='Segment')
        plt.grid(True)
        plt.savefig(os.path.join(self.config.report,'segmentation_Cluster.png'))
        plt.clf()
        
        