import pandas as pd
import logging
import os
from kaggle.api.kaggle_api_extended import KaggleApi
import boto3
from extract import kaggleUtils

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s -- %(message)s')


def downloadKaggleDataset(dataSetName):
    logging.info(f"Starting to download dataset - {dataSetName} from Kaggle")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataSetPath = os.path.join(script_dir, "../datasets/",dataSetName)
    # userName, key = kaggleUtils.getKaggleCredentials()
    # os.environ['KAGGLE_USERNAME'] = userName
    # os.environ['KAGGLE_KEY'] = key 
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataSetName, path=dataSetPath, unzip=True)
    return dataSetPath

def uploadDataAsParquetToS3(datasetPath, fileName, s3BucketName):
    df = pd.read_csv(datasetPath, encoding='ISO-8859-1')
    folder_path = os.path.dirname(datasetPath)
    filePath = os.path.join(folder_path,fileName)
    df.to_parquet(filePath)
    s3 = boto3.client('s3')
    try:
        s3.upload_file(filePath, s3BucketName, fileName)
        print(f"File uploaded successfully to {s3BucketName}/{fileName}")
    except Exception as e:
        print(f"Error uploading file: {e}")

    print("Proceeding to delete the file locally after uploading to S3")        
    if os.path.exists(filePath):
        os.remove(filePath)

    print(f"File deleted successfully from local")

    return True
    



