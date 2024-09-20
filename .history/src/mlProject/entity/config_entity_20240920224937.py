from dataclasses import dataclass
from pathlib import Path


@dataclass 
class DataIngestionConfig:
    root_dir:Path
    URL:str
    local_data_path:Path
    unzip_dir:Path
    
@dataclass
class BaseModelConfig:
    root_dir:Path
    model_path:Path
    update_model_path:Path    
    
@dataclass
class ModelTrainConfig:
    root_dir:Path
    trained_model_path:Path
    update_model_path:Path 
    training_data: Path   
    
@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int    