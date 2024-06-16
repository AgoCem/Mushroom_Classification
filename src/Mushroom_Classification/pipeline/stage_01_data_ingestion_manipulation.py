from Mushroom_Classification.config.configuration import ConfigurationManager
from Mushroom_Classification.components.data_ingestion_manipulation import DataIngestionManipulation
from Mushroom_Classification import logger


STAGE_NAME = "Data Ingestion and Manipulation"

class DataIngestionManipulationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_manipulation_config = config.get_data_ingestion_config()
        data_ingestion_manipulation = DataIngestionManipulation(config=data_ingestion_manipulation_config)
        data_ingestion_manipulation.download_file()
        data_ingestion_manipulation.preprocess_file()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionManipulationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e