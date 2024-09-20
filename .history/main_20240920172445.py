from mlProject.pipeline.stage_01_data_ingestion import *
from mlProject.pipeline.stage_02_prepare_base_model import *
from mlProject import logging

Stage_Name='Data Ingestion'
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
except Exception as e:
    logging.exception(e)
    raise e
 
Stage_Name='Base Model'
try:
    base_model=BaseModelPipeline()
    base_model.main()
except Exception as e:
    logging.exception(e)
    raise e    