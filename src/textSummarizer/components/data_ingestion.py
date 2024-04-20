import os 
import urllib.request as request
import zipfile
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_files):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, 
                filename = self.config.local_data_files
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"file already exists of size {get_size(Path(self.config.local_data_files))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_files, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)