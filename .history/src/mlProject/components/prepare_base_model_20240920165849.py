from mlProject.config.configuration import *
from mlProject import logging
import tensorflow as tf 
import os


class BaseModel:
    def __init__(self,config:BaseModelConfig) -> None:
        config=self.config
        
    def get_model(self):
            