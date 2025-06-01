from e_commerce.config.configuration import ConfigurationManager
from e_commerce.components.cluster import ClusterComponent
from e_commerce import logger

class ClusterPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        cluster_config = config.cluster_config()
        cluster_comp = ClusterComponent(config=cluster_config)
        cluster_comp.get_cluster()


STAGE_NAME = "CLUSTER FINDING" 
if __name__ == "__main__":
    try :
        logger.info(f">>>>{STAGE_NAME} started<<<<")
        obj = ClusterPipeline()
        obj.main()
        logger.info(f">>>>{STAGE_NAME} completed<<<<")

    except Exception as e:
        raise e
    