from mlProject.config.configuration import *
from mlProject import logging
import tensorflow as tf 

class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
    def train_model(self):
        self.model=tf.keras.models.load_model(self.config.update_model_path)
        
           
        