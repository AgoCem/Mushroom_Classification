
from Mushroom_Classification.utils.common import create_directories, read_yaml, save_data
from Mushroom_Classification.constants import *
from Mushroom_Classification import logger
from Mushroom_Classification.entity.config_entity import DataIngestionManipulationConfig,ModelPreparationTrainingConfig


class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root]) #the artifacts_root is the key of the dictionary created
                                                # in the yaml file and we can read this key like that instead of
                                                # ["artifacts_root"] because we used the ConfigBox in the common.py file


    def get_data_ingestion_config(self) -> DataIngestionManipulationConfig:
        config = self.config.data_ingestion_manipulation #data ingestion is the other key value of the dictionary in the config.yaml file

        create_directories([config.root_dir,config.save_training_file])

        data_ingestion_manipulation_config = DataIngestionManipulationConfig(
            root_dir=config.root_dir,
            local_data_file = config.local_data_file,
            source_URL = config.source_URL,
            save_training_file= config.save_training_file,
            param_target_col=self.params.TARGET,
            param_random_state=self.params.RANDOM_STATE
        )                                     

        return data_ingestion_manipulation_config
    

    def get_model_preparation_training_config(self) -> ModelPreparationTrainingConfig:
        config = self.config.model_preparation_training #model_preparation_training is the other key value of the dictionary in the config.yaml file

        create_directories([config.root_dir,config.save_models])

        model_preparation_training_config = ModelPreparationTrainingConfig(
            root_dir=config.root_dir,
            save_models= config.save_models,
            param_target_col=self.params.TARGET,
            param_random_state=self.params.RANDOM_STATE,
            param_n_estimators=self.params.N_ESTIMATORS,
            param_c_svc=self.params.C_SVC,
            param_gamma_svc=self.params.GAMMA_SVC,
            param_c_log_reg=self.params.C_LOG_REG,
            param_number_cv=self.params.NUMBER_CV
        )                                     

        return model_preparation_training_config