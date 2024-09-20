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
            validation_split=0.2
        )  
        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            batch_size=16,
            target_size=(224,224),
            interpolation='bilinear'
            )
        train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                rescale = 1./255,
                validation_split=0.20)
        
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            batch_size=16,
            target_size=(224,224),
            interpolation='bilinear')
        
        self.model.fit(
            self.train_generator,  
            validation_data=self.valid_generator,  
            epochs=1,  
            steps_per_epoch=len(self.train_generator),
            validation_steps=len(self.valid_generator),
            verbose=1
        )
        
        
        self.model.save(self.config.trained_model_path)