#Basic libraries
import os
import sys
from src.exception import CustomException
from src.logger import logging
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    '''This class will initiate the variables or paths required to save the data and train test split
    '''
    train_data_path:str=os.path.join('artifact','train.csv')
    test_data_path:str=os.path.join('artifact','test.csv')
    raw_data_path:str=os.path.join('artifact','data.csv')

class DataIngestion:
    ''''
    This class will read the data from the source do the train test split and save and return the path of it.
    '''
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('data ingestion has started')

        try:
            df=pd.read_csv('Notebook\data\stud.csv')
            #Here the code can be changed to read the data from multiple sources.
            logging.info('read the dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('train test split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Train test and raw data saved')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)


    
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

