from e_commerce.components.model import ModelBuildingComponent
from e_commerce.config.configuration import ConfigurationManager
from e_commerce import logger 
class ModelPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_config = config.get_model_config()
        model_build_comp = ModelBuildingComponent(config=model_config)
        model_build_comp.build_model()



STAGE_NAME = "MODEL BUILDING"
if __name__ == "__main__":
    try :
        logger.info(f">>>>{STAGE_NAME} started<<<<")
        obj = ModelPipeline()
        obj.main()
        logger.info(f">>>>{STAGE_NAME} completed<<<<")
    except Exception as e:
        raise e
    
