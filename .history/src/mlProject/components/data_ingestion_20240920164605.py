from mlProject.config.configuration import *
from mlProject import logging
import zipfile,os
import urllib.request as request


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
                request.urlretrieve(self.config.URL,self.config.local_data_path)
                logging.info('Download Zip Data')
                
        else:
            logging.info('File Alredy exists')        
            
    def extract_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_path,'r') as f:
            f.extractall(unzip_path)
            logging.info('Extract All Data')        