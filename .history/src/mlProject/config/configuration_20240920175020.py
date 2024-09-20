from mlProject.entity.config_entity import *
from mlProject import logging
import zipfile,os
from mlProject.utils.common import *
from mlProject.constants import *

class ConfigurationManager:
    def __init__(self):
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self):
        config=self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestionn_config=DataIngestionConfig(
            root_dir=config.root_dir,
            URL=config.URL,
            local_data_path=config.local_data_path,
            unzip_dir=config.unzip_dir
        )    
        
        return data_ingestionn_config
    
    def get_base_model_path_config(self):
        config=self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        prepare_base_model_config=BaseModelConfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            update_model_path=config.update_model_path
        )
        return prepare_base_model_config
    
    def get_model_train_config(self):
        config=self.config.model_train
        
        create_directories([config.root_dir])
        
        model_train_config=ModelTrainConfig(
            root_dir=config.root_dir,
            train_model_path=config.train_model_path
        )
        return model_train_config