from e_commerce.utils.common import read_yaml , create_directories 
from e_commerce.constants import *
from e_commerce.entity.config_entity import DataIngestionconfig,PreProcessing,FeatureEngineeringconfig,EDA,outlier,cluster,model,prediction

class ConfigurationManager:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionconfig:
        config = self.config.data_ingestion
        data_ingestion_config = DataIngestionconfig(root_dir=config.root_dir,
                                                    source_url=config.source_url,
                                                    local_data_file=config.local_data_file)
        return data_ingestion_config
    
    def get_preprocessing_config(self)->PreProcessing:
        config = self.config.pre_processing
        create_directories([config.cleaned_data_save_path])
        create_directories([config.data_report])
        pre_processing_config = PreProcessing(data_path=config.data_path,cleaned_data_save_path=config.cleaned_data_save_path,data_report=config.data_report
                                              )
        return pre_processing_config
    
    def get_feature_engg_config(self)->FeatureEngineeringconfig:
        config = self.config.feature_engg
        create_directories([config.output_path])
        feature_engg_config = FeatureEngineeringconfig(data_path=config.data_path,output_path=config.output_path)
        return feature_engg_config 
    
    def get_eda_config(self)->EDA:
        config = self.config.EDA
        create_directories([config.report])
        eda_config = EDA(data_path=config.data_path,report=config.report)

        return eda_config
    
    def outlier_config(self)->outlier:
        config = self.config.outlier
        create_directories([config.output_path])
        create_directories([config.report])
        outlier_config = outlier(data_path=config.data_path,output_path=config.output_path,report=config.report)
        return outlier_config
    def cluster_config(self)->cluster:
        config = self.config.cluster
        params = self.params.cluster
        create_directories([config.cluster])
        create_directories([config.report])
        cluster_config = cluster(data_path=config.data_path,cluster=config.cluster,report=config.report,random_state= params.random_state)
        return cluster_config
    def get_model_config(self)->model:
        config = self.config.model
        params = self.params.model
        create_directories([config.models])
        create_directories([config.report])
        model_config = model(data_path=config.data_path,original_data=config.original_data,kl_path=config.kl_path,models=config.models,report=config.report,random_state=params.random_state)
        return model_config
    def prediction_config(self)->prediction:
        config = self.config.prediction
        prediction_config = prediction(model_path=config.model_path,scaler_path=config.scaler_path)
        return prediction_config