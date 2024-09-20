from mlProject.config.configuration import *
from mlProject import logging
import tensorflow as tf 

class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
    def train_model(self):
        self.model=tf.keras.models.load_model(self.config.update_model_path)
        
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1/255,
            validation_split=0.2,
            horizontal_flip=True,
            zoom_range=0.1,
            rotation_range=0.1
        )   
        