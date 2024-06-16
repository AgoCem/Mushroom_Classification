import os
from box.exceptions import BoxValueError
import yaml
from Mushroom_Classification import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import dill
import pandas as pd




@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox: #the ConfigBox is useful to call in an easier and more direct
                                                # way the dictionaries and here i tell him read
                                                # everything as a ConfigBox
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations #a decorator from the ensure module and here i want him to be sure that the annotation i'm giving are respected such as list type and so on
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path_dir in path_to_directories:
        if not os.path.exists(path_dir):
            os.makedirs(path_dir, exist_ok=True)
            logger.info(f"created directory at: {path_dir}")
        else:
            logger.info(f"The directory {path_dir} already exists")


@ensure_annotations
def save_data(path_to_data_dir: Path, data, name: str):
    """Save Data in a given directory

    Args :
        path where to save data
        data to save
        name of the data
        
    """
    
    original_dir = os.getcwd()  # Save the original working directory
    
    
    try:
        # Ensure the directory exists
        if not path_to_data_dir.exists():
            
            path_to_data_dir.mkdir(parents=True, exist_ok=True)
        
        os.chdir(path_to_data_dir)  # Change the working directory to the target path
        

        # Save the data to a CSV file in the current directory
        data.to_csv(name, index=False, header=True)
        logger.info(f"File {name} saved")
        
    except Exception as e:
        raise e  
    
    finally:
        os.chdir(original_dir)  # Change back to the original directory
        
@ensure_annotations
def read_file(file_path: Path,file:str):
        """
        Read the csv file
        """

        original_dir = os.getcwd() 
        try:
            os.chdir(file_path)
            data = pd.read_csv(file)
            os.chdir(original_dir)
            return data

        except Exception as e:
            e


@ensure_annotations
def save_object(file_path: Path,obj,name):
    """Save a model in a given directory
    
    Args :
        path where to save object
        object to save
        
    """
    try:
        os.makedirs(file_path, exist_ok=True)
        original_dir = os.getcwd()
        
        os.chdir(file_path)

        with open(name,"wb") as file_obj:
            dill.dump(obj, file_obj) #the dill is a package that extends the capabilities of the pickle module
                                    # basically we can save function, classes, objects etc. Here we want
                                    # to save a given obj and this is a function that will be called from multiple
                                    # files, for example we can save models etc.. 

    except Exception as e:
        raise e
    finally:
        os.chdir(original_dir)
    
@ensure_annotations
def load_object(file_path: Path):
    """Load a model from a given directory
    
    Args :
        path where to load object
        object to load
        
    """
    try:
        
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise e