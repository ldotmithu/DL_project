from mlProject.components.data_ingestion import *
from mlProject.config.configuration import *


class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_ingestionn_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestionn_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()