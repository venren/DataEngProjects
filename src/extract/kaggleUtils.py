import json
import os
import logging
from kaggle.api.kaggle_api_extended import KaggleApi

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s -- %(message)s')

## below function is not used as we currently store kaggle.json in user folder
## as required by kaggle API
def getKaggleCredentials():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'kaggle.json')  # Navigate up to project and then to data
        with open(file_path, "r") as f:
            kaggle_auth = json.load(f)
            username = kaggle_auth["username"]
            key = kaggle_auth["key"]
            return(username, key)
    except FileNotFoundError:
        print(f"Json file not found")
        return(None, None)
    except json.JSONDecodeError:
        print(f"Not a valid json")

def downloadKaggleDataset(dataSetName):
    logging.info(f"Starting to download dataset - {dataSetName} from Kaggle")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataSetPath = os.path.join(script_dir, "../datasets/",dataSetName)
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataSetName, path=dataSetPath, unzip=True)
    return dataSetPath
