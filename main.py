from Mushroom_Classification import logger
from Mushroom_Classification.pipeline.stage_01_data_ingestion_manipulation import DataIngestionManipulationPipeline
from Mushroom_Classification.pipeline.stage_02_model_preparation_training import ModelPreparationTrainingPipeline


STAGE_NAME = "Data Ingestion and Manipulation"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_manipulation = DataIngestionManipulationPipeline()
    data_ingestion_manipulation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Preparation Training"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_preparation_training = ModelPreparationTrainingPipeline()
    model_preparation_training.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e