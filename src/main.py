from extract import start
import os
from datetime import datetime

current_date = datetime.now()
date_str = current_date.strftime("%Y-%m-%d")
fileName = f"ecommerce-dataset_{date_str}.parquet"
filePath = os.path.join(os.path.dirname(__file__),"datasets/carrie1/ecommerce-data/data.csv")
start.downloadKaggleDataset("carrie1/ecommerce-data")
start.uploadDataAsParquetToS3(filePath,fileName,"project-1-aws-etl")