from Mushroom_Classification.config.configuration import ConfigurationManager
from Mushroom_Classification.components.model_preparation_training import ModelPreparationTraining
from Mushroom_Classification import logger



STAGE_NAME = "Model Preparation Training"

class ModelPreparationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_preparation_training_config = config.get_model_preparation_training_config()
        model_preparation_training = ModelPreparationTraining(config=model_preparation_training_config)
        model_preparation_training.model_preparation_training()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelPreparationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e