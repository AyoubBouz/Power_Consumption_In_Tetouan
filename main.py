from powerconsumptiontetouan import logger
from powerconsumptiontetouan.pipeline.stage_data_ingestion import DataIngestionTrainingPipeline
from powerconsumptiontetouan.pipeline.stage_data_validation import DataValidationTrainingPipeline
# logger.info("Welcome back Bro !")


STAGE_NAME = "Data Ingestion"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e