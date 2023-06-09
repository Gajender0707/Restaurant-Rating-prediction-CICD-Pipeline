from logger import logging
from exception import CustomException
import os
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split
import mysql.connector as connection
from data_transformation import DataTransformation,DataTransformationConfig
from model_trainer import ModelTrainerConfig,ModelTrainer

@dataclass
class DataIngestionConfig:
    row_data_path=os.path.join(os.getcwd(),"Artifacts","row_data.csv")
    train_data_path=os.path.join(os.getcwd(),"Artifacts","train.csv")
    test_data_path=os.path.join(os.getcwd(),"Artifacts","test.csv")
    logging.info("give the row data,train and test path to store the data.")


class DataIngestion:

    def __init__(self):
        self.data_ingestion_paths=DataIngestionConfig()
        
    def Initiate_data_ingestion(self):
        try:

            # data=pd.read_csv(r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Restaurant-Rating-Prediction\data\Zomato_data.csv")
            mydb = connection.connect(host="localhost", database = 'zomato',user="root", passwd="Gajender@123",use_pure=True)
            logging.info("set the connection with the mysql for read the data")
            query = "select online_order,book_table,rate,votes,rest_type,cost,type,city from zomato.zomato_5k;"
            logging.info(f"select the column which we need for the dataset: {query}")
            result_dataFrame = pd.read_sql(query,mydb)
            mydb.close()
            data=result_dataFrame
            logging.info("read the data")
            train_data,test_data=train_test_split(data,test_size=0.2,random_state=42)
            logging.info("split the data into train and test")

            os.makedirs(os.path.dirname(self.data_ingestion_paths.row_data_path),exist_ok=True)
            logging.info("Created the Artifacts folder for the save the train and test data")
            data.to_csv(self.data_ingestion_paths.row_data_path)
            train_data.to_csv(self.data_ingestion_paths.train_data_path)
            test_data.to_csv(self.data_ingestion_paths.test_data_path)
            logging.info("train test and row data has been saved in artifacts folder")

            return (self.data_ingestion_paths.train_data_path,
                    self.data_ingestion_paths.test_data_path)
        except Exception as e:
            raise CustomException(e)
        
if __name__=="__main__":
    data_ingestion_obj=DataIngestion()
    train_path,test_path=data_ingestion_obj.Initiate_data_ingestion()
    data_transformation_obj=DataTransformation()
    x_train_array,y_train_array,x_test_array,y_test_array=data_transformation_obj.Intiate_data_transformation(train_data_path=train_path,test_data_path=test_path)
    model_trainer_obj=ModelTrainer()
    model_trainer_obj.Initiate_model_training(x_train_array=x_train_array,y_train_array=y_train_array,x_test_array=x_test_array,y_test_array=y_test_array)
