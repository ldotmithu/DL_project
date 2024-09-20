from mlProject.config.configuration import *
from mlProject import logging
import zipfile,os
import urllib.request as request


import os
import logging
import zipfile
from urllib import request

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
            request.urlretrieve(self.config.URL, self.config.local_data_path)
            logging.info('Downloaded Zip Data')
        else:
            logging.info('File already exists')        
            
    def extract_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        # Check if the file is indeed a zip file
        if not self.config.local_data_path.endswith('.zip'):
            logging.error(f"Expected a zip file but got: {self.config.local_data_path}")
            raise ValueError("The specified file is not a zip file.")
        
        # Attempt to extract the zip file
        try:
            with zipfile.ZipFile(self.config.local_data_path, 'r') as f:
                f.extractall(unzip_path)
                logging.info('Extracted all data')
        except zipfile.BadZipFile:
            logging.error(f"File is not a zip file: {self.config.local_data_path}")
            raise

