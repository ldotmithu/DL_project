from mlProject.components.prepare_base_model import *
from mlProject.config.configuration import *

class BaseModelPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        base_model_config=config.get_base_model_path_config()
        base_model=BaseModel(config=base_model_config)
        base_model.get_model()