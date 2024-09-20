from mlProject.config.configuration import *
from mlProject import logging
import tensorflow as tf 
import os
from mlProject.utils.common import *


class BaseModel:
    def __init__(self, config: BaseModelConfig):
        self.config = config
        
    def get_model(self):
        self.model = tf.keras.applications.VGG16(
            input_shape=(224, 224, 3),
            weights='imagenet',
            include_top=False
        )    
        
        for layer in self.model.layers:
            layer.trainable = False
       
        x = tf.keras.layers.Flatten()(self.model.output)  
        prediction = tf.keras.layers.Dense(units=2, activation="softmax")(x)
        
        # Create the model
        model = tf.keras.models.Model(inputs=self.model.input, outputs=prediction)
        
        # Compile the model
        model.compile(optimizer='adam', loss=tf.keras.losses.CategoricalCrossentropy(), metrics=["accuracy"])  # Fix 'optimize' to 'optimizer'
        
        # Print model summary
        model.summary()
        
        # Save the model
        model.save(self.config.update_model_path)  # Correct save method
        
        return model
