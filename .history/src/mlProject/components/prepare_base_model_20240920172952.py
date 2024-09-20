from mlProject.config.configuration import *
from mlProject import logging
import tensorflow as tf 
import os
from mlProject.utils.common import *



class BaseModel:
    def __init__(self,config:BaseModelConfig):
        self.config=config
        
    def get_model(self):
        self.model=tf.keras.applications.VGG16(
            input_shape=(224,224,3),
            weights='imagenet',
            include_top=False
        )    
        
        for layer in self.model.layers:
            layer.trainable=False
            
        model=tf.keras.layers.Flatten()(self.model)
        prediction=tf.keras.layers.Dense(units=2,activation="softmax")(model)
        
        model=tf.keras.models.Model(inputs=self.model.input,outputs=prediction)
        
        model=compile(optimize='adam',loss=tf.keras.losses.CategoricalCrossentropy(),metrics=["accuracy"])
        
        model.summary()
        
        self.save.model(model,self.config.update_model_path)
    

        
            
             