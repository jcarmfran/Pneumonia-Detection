from pneuDetection import logger
from pneuDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from pneuDetection.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from pneuDetection.pipeline.stage_03_model_training import ModelTrainingPipeline
from pneuDetection.pipeline.stage_04_model_evaluation import EvaluationPipeline


### DATA INGESTION STAGE ###

STAGE_NAME = "DATA INGESTION"

try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e


### DATA PREPARATION STAGE ###

STAGE_NAME = "DATA PREPARATION"

try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e


### DATA TRAINING STAGE ###

STAGE_NAME = "MODEL TRAINING"

try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e


### MODEL EVALUATION STAGE ###

STAGE_NAME = "MODEL EVALUATION"

try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = EvaluationPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e