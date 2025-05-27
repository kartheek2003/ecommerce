from e_commerce import logger
import os
from e_commerce.pipeline.stage01_data_ingestion import DataIngestionPipeline

STAGE_NAME ="DATA INGESTION"

try :
    logger.info(f">>>>{STAGE_NAME} started<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>{STAGE_NAME} completed<<<<")

except Exception as e:
    raise e