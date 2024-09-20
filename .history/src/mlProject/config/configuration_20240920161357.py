from mlProject.entity.config_entity import *
from mlProject import logging
import zipfile,os
from mlProject.utils.common import *
from mlProject.constants import *

class ConfigurationManager:
    def __init__(self):
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)