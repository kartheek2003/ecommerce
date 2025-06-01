
from e_commerce import logger
import os
from e_commerce.pipeline.stage01_data_ingestion import DataIngestionPipeline
from e_commerce.pipeline.stage02_pre_processing import PreProcessingPipeline
from e_commerce.pipeline.stage03_feature_engg_pipeline import FeatureEnggPipeline
from e_commerce.pipeline.stage04_EDA import EDAPipeline
from e_commerce.pipeline.stage05_outlier import OutierPipeline
from e_commerce.pipeline.stage06_cluster import ClusterPipeline
from e_commerce.pipeline.stage07_model import ModelPipeline

print("Starting main.py execution from the top")

STAGE_NAME ="DATA INGESTION"

try :
    logger.info(f">>>>{STAGE_NAME} started<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>{STAGE_NAME} completed<<<<")

except Exception as e:
    raise e



STAGE_NAME = "PRE PROCESSING"

try:
    logger.info(f">>>>{STAGE_NAME} started<<<<")
    obj = PreProcessingPipeline()
    obj.main()
    logger.info(f">>>>{STAGE_NAME} completed<<<<")
except Exception as e:
    raise e


STAGE_NAME = "FEATURE ENGINEERING"
try :
    logger.info(f">>>>{STAGE_NAME} STARTED <<<<")
    obj = FeatureEnggPipeline()
    obj.main()
    logger.info(f">>>>{STAGE_NAME} COMPLETED <<<<")
except Exception as e :
    raise e


STAGE_NAME = "EDA"
try :
    logger.info(f">>>>{STAGE_NAME} STARTED<<<<")
    obj = EDAPipeline()
    obj.main()
    logger.info(f">>>>{STAGE_NAME} COMPLETED<<<<")
except Exception as e:
    raise e

STAGE_NAME = "OUTLIER REMOVAL"
try:
    logger.info(f">>>>{STAGE_NAME} started<<<<")
    obj = OutierPipeline()
    obj.main()
    logger.info(f">>>>{STAGE_NAME}completed<<<<")
except Exception as e:
    raise e

STAGE_NAME = "CLUSTER FINDING" 

try :
    logger.info(f">>>>{STAGE_NAME} started<<<<")
    obj = ClusterPipeline()
    obj.main()
    logger.info(f">>>>{STAGE_NAME} completed<<<<")

except Exception as e:
    raise e

STAGE_NAME = "MODEL BUILDING"

try :
    logger.info(f">>>>{STAGE_NAME} started<<<<")
    obj = ModelPipeline()
    obj.main()
    logger.info(f">>>>{STAGE_NAME} completed<<<<")
except Exception as e:
    raise e