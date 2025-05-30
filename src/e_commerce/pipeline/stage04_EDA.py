from e_commerce.config.configuration import ConfigurationManager
from e_commerce.components.EDA import EDAComponent
from e_commerce import logger


class EDAPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        eda_config = config.get_eda_config()
        eda_comp = EDAComponent(config=eda_config)
        eda_comp.get_EDA()


STAGE_NAME = "EDA"
try :
    logger.info(f">>>>{STAGE_NAME} STARTED<<<<")
    obj = EDAPipeline()
    obj.main()
    logger.info(f">>>>{STAGE_NAME} COMPLETED<<<<")
except Exception as e:
    raise e
