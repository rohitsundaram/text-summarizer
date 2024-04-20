import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """

    :param path_to_yaml: path like input
    :return: ConfigBox: ConfigBox type
    :Args: path_to_yaml (str): path like input

    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    Create list of directories
    :param path_to_directories: list of path of directories
    :param verbose:
    :return:
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")

@ensure_annotations
def get_size(path:Path) -> str:
    """
    get size in KB
    :param path: path of the file
    :return:
    str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"