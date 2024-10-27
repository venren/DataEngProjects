import pandas as pd
import logging
from my_kaggle import kaggleUtils
import os
from kaggle.api.kaggle_api_extended import KaggleApi

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s -- %(message)s')


def downloadKaggleDataset(dataSetName):
    logging.info(f"Starting to download dataset - {dataSetName} from Kaggle")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataSetPath = os.path.join(script_dir, "../datasets/",dataSetName)
    userName, key = kaggleUtils.getKaggleCredentials()
    os.environ['KAGGLE_USERNAME'] = userName
    os.environ['KAGGLE_KEY'] = key 
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataSetName, path=dataSetPath, unzip=True)
    return dataSetPath
    



