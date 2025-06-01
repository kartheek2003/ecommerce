import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import joblib
from sklearn.cluster import KMeans
from kneed import KneeLocator
import os 
from e_commerce.entity.config_entity import cluster
class ClusterComponent:
    def __init__(self,config : cluster):
        self.config = config
        
    def load_data(self):
        if not os.path.exists(self.config.data_path):
            raise FileNotFoundError(f"Input file not found: {self.config.data_path}")
        return pd.read_csv(self.config.data_path)

    def get_cluster(self):
        df = self.load_data()
        rmf = df[['recency','frequency','monetary']]
        # scaling
        scaler = MinMaxScaler()
        rmf_scaled = scaler.fit_transform(rmf)
        rmf_scaled = pd.DataFrame(data=rmf_scaled, columns=['recency', 'frequency', 'monetary'])
        rmf_scaled.to_csv(os.path.join(self.config.cluster,"rmf_scaled.csv"),index=False)
        joblib.dump(scaler,os.path.join(self.config.cluster,'scaler.pkl'))

        # elbow method
        sse = []
        k_range = range(1,10)
        for k in k_range:
            km = KMeans(n_clusters=k,random_state=self.config.random_state)
            km.fit(rmf_scaled[['recency','monetary']])
            sse.append(km.inertia_)
        with open(os.path.join(self.config.report,"sse_info.txt"),'w') as f:
            for i, val in enumerate(sse, start=1):
                f.write(f"k={i}, SSE={val}\n")
            

        # knee locator 
        kl = KneeLocator(
            x= k_range,
            y=sse,
            curve='convex',
            direction='decreasing'
        )
        with open(os.path.join(self.config.report,'knee_elbow.txt'),'w') as f:
            f.write(f'optimal no of clusters (elbow) : {kl.elbow}')

        print(f"Optimal number of clusters (elbow): {kl.elbow}")
        joblib.dump(kl,os.path.join(self.config.cluster,'kneelocator.pkl'))

        # Plot the elbow graph
        plt.plot(k_range, sse, marker='o')
        plt.axvline(x=kl.elbow, color='red', linestyle='--', label=f'Elbow at k={kl.elbow}')
        plt.xlabel('Number of Clusters')
        plt.ylabel('SSE')
        plt.title('Elbow Method with KneeLocator')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(self.config.report,"elbow_graph.png"))
        plt.clf()

