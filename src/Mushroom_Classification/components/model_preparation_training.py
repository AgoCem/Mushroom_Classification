from Mushroom_Classification.utils.common import create_directories, read_yaml, save_object, read_file
from Mushroom_Classification.constants import *
from Mushroom_Classification import logger
from pathlib import Path
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from Mushroom_Classification.entity.config_entity import ModelPreparationTrainingConfig
import pandas as pd

class ModelPreparationTraining:
    def __init__(self, config: ModelPreparationTrainingConfig):
        self.config = config


    def model_preparation_training(self):
        """Stage of model preparation and training"""

        train_file = "train.csv"
        train_pca_file = "train_pca.csv"

        train = read_file(Path(self.config.root_dir),train_file)
        train_pca = read_file(Path(self.config.root_dir),train_pca_file)
        X_train = train.drop(columns=self.config.param_target_col, axis = 1)
        y_train = train[self.config.param_target_col]
        X_train_pca = train_pca.drop(columns=self.config.param_target_col, axis = 1)
        y_train_pca = train_pca[self.config.param_target_col]


        model_params = {
                'rnd_for':{
                    'model' : RandomForestClassifier(random_state=self.config.param_random_state),
                    'params':{
                        'n_estimators':self.config.param_n_estimators
                    }
                },
                'log_reg':{
                    'model': LogisticRegression(max_iter = 5000),
                    'params': {
                        'C':self.config.param_c_log_reg
                    }
                },
                'svm':{
                    'model': SVC(),
                    'params':{
                        'gamma':self.config.param_gamma_svc,
                        'C':self.config.param_c_svc
                    }
                }
                }
        
        best_models=[]

        logger.info("Performing GridSearch\n")

        for model,model_param in model_params.items():
            grid = GridSearchCV(model_param['model'], model_param['params'], cv = 5)
            grid.fit(X_train,y_train)
            best_models.append({
                'model':model,
                'best_params':grid.best_params_,
                'best_score':grid.best_score_
            })

        best_model_df = pd.DataFrame(best_models)
        ind = best_model_df.best_score.idxmax()
        model =best_model_df.iloc[ind]["model"]
        param =best_model_df.iloc[ind]["best_params"]
        models = {
                'rnd_for': RandomForestClassifier(random_state=self.config.param_random_state),
                'log_reg': LogisticRegression(max_iter = 5000),
                'svm':SVC(),
                }
        logger.info(f"The chosen model is {model} with the following parameters: {param}")
        final_model = models[best_model_df.iloc[ind]["model"]]
        final_model.set_params(**param)
        final_model.fit(X_train,y_train)
        save_object(Path(self.config.save_models),final_model,"best_model.pkl")

        final_model_pca = models[best_model_df.iloc[ind]["model"]]
        final_model_pca.set_params(**param)
        final_model_pca.fit(X_train_pca,y_train_pca)
        save_object(Path(self.config.save_models),final_model,"pca_model.pkl")

        return None