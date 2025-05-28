from e_commerce.config.configuration import ConfigurationManager
from e_commerce.components.feature_engg import FeatureEnggComponent
from e_commerce import logger
class FeatureEnggPipeline:
    def __call__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        feature_engg_config = config.get_feature_engg_config()
        feature_engg_comp = FeatureEnggComponent(config=feature_engg_config)
        feature_engg_comp.feature_engg()


STAGE_NAME = "FEATURE ENGINEERING"

if __name__ == "__main__":
    try :
        logger.info(f">>>>{STAGE_NAME} STARTED <<<<")
        obj = FeatureEnggPipeline()
        obj.main()
        logger.info(f">>>>{STAGE_NAME} COMPLETED <<<<")

    except Exception as e:
        raise e
    
