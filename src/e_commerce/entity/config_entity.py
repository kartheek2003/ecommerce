from dataclasses import dataclass
from pathlib import Path
@dataclass
class DataIngestionconfig:
  root_dir : Path
  source_url : str
  local_data_file : Path

@dataclass 
class PreProcessing:
  data_path : Path
  data_report : Path
  cleaned_data_save_path :Path

@dataclass
class FeatureEngineeringconfig:
  data_path : Path 
  output_path : Path
  

@dataclass
class EDA:
  data_path : Path
  report : Path

@dataclass
class outlier :
  data_path : Path
  output_path: Path
  report : Path
  
@dataclass
class cluster :
  data_path : Path
  cluster : Path
  report : Path
  random_state : int

@dataclass
class model : 
  data_path : Path
  original_data : Path
  kl_path : Path
  models : Path
  report : Path
  random_state : int

@dataclass
class prediction:
  model_path : Path
  scaler_path : Path
  
