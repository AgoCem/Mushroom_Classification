from Mushroom_Classification import logger
from Mushroom_Classification.pipeline.stage_01_data_ingestion_manipulation import DataIngestionManipulationPipeline


STAGE_NAME = "Data Ingestion and Manipulation"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_manipulation = DataIngestionManipulationPipeline()
    data_ingestion_manipulation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e