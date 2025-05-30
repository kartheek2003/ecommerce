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

  