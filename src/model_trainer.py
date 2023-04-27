import pandas as pd
from logger import logging
from exception import CustomException
from dataclasses import dataclass
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import os
from utils import save_object,model_training

@dataclass
class ModelTrainerConfig:
    model_path=os.path.join("Artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_saving_path=ModelTrainerConfig()
        logging.info("define the model saving path")

    def Initiate_model_training(self,x_train_array,y_train_array,x_test_array,y_test_array):
        try:
            self.x_train_array=x_train_array
            self.y_train_array=y_train_array
            self.x_test_array=x_test_array
            self.y_test_array=y_test_array
            logging.info("Define the training and testing array for x and y")
            models={
                "RandomForestClassifier":RandomForestClassifier(),
            "DecisionTreeClassifier":DecisionTreeClassifier(),
                "KNeighborsClassifier":KNeighborsClassifier(),
                    "LogisticRegression":LogisticRegression()}
            logging.info("Models Are defined Successfully.")
            
            score_report=model_training(models,x_train_array,y_train_array,x_test_array,y_test_array)
            logging.info(f"Score report has been recieved which has the score and model respectivly : {score_report}")
            
            ##HypertuneParamter
            



        except Exception as e:
            raise CustomException(e)