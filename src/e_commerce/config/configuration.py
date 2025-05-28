from e_commerce.utils.common import read_yaml , create_directories 
from e_commerce.constants import *
from e_commerce.entity.config_entity import DataIngestionconfig,PreProcessing,FeatureEngineeringconfig

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