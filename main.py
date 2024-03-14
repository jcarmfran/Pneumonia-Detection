from pneuDetection import logger
from pneuDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


### DATA INGESTION STAGE ###

STAGE_NAME = "Data Ingestion Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e