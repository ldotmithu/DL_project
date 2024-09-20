from mlProject.config.configuration import *
from mlProject import logging
import zipfile,os


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
        