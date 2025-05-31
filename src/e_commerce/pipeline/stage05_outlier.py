from e_commerce.config.configuration import ConfigurationManager
from e_commerce.components.outlier_removal import OutlierComponent
from e_commerce import logger

class OutierPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        outlier_Config = config.outlier_config()
        outlier_comp = OutlierComponent(config=outlier_Config)
        outlier_comp.outlier_removal()

STAGE_NAME = "OUTLIER REMOVAL"
if __name__ == "__main__":
    try:
        logger.info(f">>>>{STAGE_NAME} started<<<<")
        obj = OutierPipeline()
        obj.main()
        logger.info(f">>>>{STAGE_NAME}completed<<<<")
    except Exception as e:
        raise e
    