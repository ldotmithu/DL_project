from mlProject.config.configuration import *
from mlProject import logging
import zipfile
import os
import urllib.request as request


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
            try:
                request.urlretrieve(self.config.URL, self.config.local_data_path)
                logging.info('Download completed: Zip Data downloaded.')
            except Exception as e:
                logging.error(f'Error occurred during file download: {e}')
        else:
            logging.info('File already exists.')
            
    def extract_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        # Check if the files have already been extracted
        if not os.listdir(unzip_path):  # If the directory is empty
            try:
                with zipfile.ZipFile(self.config.local_data_path, 'r') as f:
                    f.extractall(unzip_path)
                    logging.info('Extracted all data.')
            except zipfile.BadZipFile:
                logging.error('Error: Bad zip file.')
            except Exception as e:
                logging.error(f'Error occurred during extraction: {e}')
        else:
            logging.info('Data already extracted.')
