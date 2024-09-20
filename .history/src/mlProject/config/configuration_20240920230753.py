from mlProject.entity.config_entity import *
from mlProject import logging
import zipfile,os
from mlProject.utils.common import *
from mlProject.constants import *

class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
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
        training = self.config.training
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chest-CT-Scan-data")
        create_directories([
            Path(training.root_dir)
        ])
        
        model_train_config=ModelTrainConfig(
            root_dir=training.root_dir,
            trained_model_path=training.trained_model_path,
            update_model_path=training.update_model_path,
            training_data=Path(training_data)
        )
        return model_train_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts\data_ingestion\Chest-CT-Scan-data",
            mlflow_uri="https://dagshub.com/ldotmithu/DL_project.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config