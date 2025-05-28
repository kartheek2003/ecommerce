from e_commerce import logger
import os
from e_commerce.pipeline.stage01_data_ingestion import DataIngestionPipeline
from e_commerce.pipeline.stage02_pre_processing import PreProcessingPipeline
from e_commerce.pipeline.stage03_feature_engg_pipeline import FeatureEnggPipeline

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

