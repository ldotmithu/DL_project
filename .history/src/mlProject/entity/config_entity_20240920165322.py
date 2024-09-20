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