from textSummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarization.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started")
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e