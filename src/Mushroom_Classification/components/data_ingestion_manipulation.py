import urllib.request as request
from Mushroom_Classification.entity.config_entity import DataIngestionManipulationConfig
from Mushroom_Classification import logger
import pandas as pd
import os
from sklearn.preprocessing import OrdinalEncoder, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from Mushroom_Classification.utils.common import save_data,read_file
from pathlib import Path




class DataIngestionManipulation:
    def __init__(self, config: DataIngestionManipulationConfig):
        self.config = config

    def download_file(self):
        """
        file_path: str
        Download, if it doesn't already exists, the csv file with data, don't need a return, just to save the Data
        """
        file = "mushrooms.csv" 
        new_path = os.path.join(self.config.local_data_file,file)
        if not os.path.exists(new_path):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= new_path
            )

            logger.info(f"{file} is downloading!")
        else:
            logger.info(f"File already downloaded")
        
        return None
    

    def preprocess_file(self):
        """
        Preprocess the data and save it into a training and testing files
        """
        raw_data = read_file(Path(self.config.local_data_file), "mushrooms.csv")
        numerical_cols = raw_data.select_dtypes(include='number').columns
        categorical_cols = raw_data.select_dtypes(include='object').columns

        
        encoder = OrdinalEncoder()
        raw_data[categorical_cols] = encoder.fit_transform(raw_data[categorical_cols])

        X = raw_data.drop(labels = self.config.param_target_col, axis = 1)
        y = raw_data[self.config.param_target_col]
        
        scaler = RobustScaler()
        numerical_cols = X.select_dtypes(include='number').columns
        X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state= self.config.param_random_state)

        train_data = pd.concat([X_train,y_train],axis = 1)
        test_data = pd.concat([X_test,y_test],axis = 1)

        pca = PCA(n_components=5)
        X_train_pca = pca.fit_transform(X_train) 
        X_test_pca = pca.transform(X_test) 
        X_train_pca = pd.DataFrame(X_train_pca)
        X_test_pca = pd.DataFrame(X_test_pca)

        train_pca_data = pd.concat([X_train_pca,y_train],axis = 1)
        test_pca_data = pd.concat([X_test_pca,y_test],axis = 1)
        

        training_path = self.config.save_training_file 
        save_data(Path(training_path),train_data,"train.csv")
        save_data(Path(training_path),test_data,"test.csv")
        save_data(Path(training_path),train_pca_data,"train_pca.csv")
        save_data(Path(training_path),test_pca_data,"test_pca.csv")
        
        return None