from mlProject.config.configuration import *
from mlProject import logging
import tensorflow as tf 
import os
from mlProject.utils.common import *
from tensorflow.keras.


class BaseModel:
    def __init__(self,config:BaseModelConfig) -> None:
        config=self.config
        
    def get_model(self):
        self.model=tf.keras.applications.VGG16(
            input_shape=(224,224,3),
            weights='imagenet',
            include_top=False
        )    
        
        for layer in self.model.layers:
            layer.trainable=False
            
        X=    
            
             