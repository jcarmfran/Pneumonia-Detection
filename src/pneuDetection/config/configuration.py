from pneuDetection.constants import *
import os
from pneuDetection.utils.common import read_yaml, create_directories, save_json
from pneuDetection.entity.config_entity import (DataIngestionConfig,
                                                PrepareBaseModelConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,  # src/pneuDetection/constants/__init__.py >> config.yaml
        params_filepath = PARAMS_FILE_PATH): # src/pneuDetection/constants/__init__.py >> params.yaml

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root]) # creating artifacts folder


    ### INGESTION ###
    def get_data_ingestion_config(self) -> DataIngestionConfig: # DataIngestionConfig type: root_dir, source_URL, local_data_file, unzip_dir
        config = self.config.data_ingestion # extracting data_ingestion from config.yaml

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config


    ### PREPARATION ### 
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config