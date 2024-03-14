from pneuDetection.constants import *
import os
from pneuDetection.utils.common import read_yaml, create_directories, save_json
from pneuDetection.entity.config_entity import (DataIngestionConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,  # src/pneuDetection/constants/__init__.py >> config.yaml
        params_filepath = PARAMS_FILE_PATH): # src/pneuDetection/constants/__init__.py >> params.yaml

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root]) # creating artifacts folder


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