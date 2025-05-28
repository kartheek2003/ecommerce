from e_commerce.config.configuration import ConfigurationManager
from e_commerce.components.pre_processing import PreProcessingComponent
from e_commerce import logger
class PreProcessingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_preprocessing_config = config.get_preprocessing_config()
        pre_process_component = PreProcessingComponent(config=data_preprocessing_config)
        pre_process_component.data_cleaning()

STAGE_NAME = "PRE PROCESSING"
if __name__ == "__main__":
    try:
        logger.info(f">>>>{STAGE_NAME} started<<<<")
        obj = PreProcessingPipeline()
        obj.main()
        logger.info(f">>>>{STAGE_NAME} completed")

    except Exception as e:
        raise e