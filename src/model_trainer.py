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
        
            
            ##HypertuneParamter
            param={
                "RandomForestClassifier":{
            'criterion':['log_loss', 'gini', 'entropy'],
                    'max_features':['sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256] },
        
                "DecisionTreeClassifier":{
           'criterion':['log_loss', 'gini', 'entropy'],
                    'splitter':['best','random'],
                    'max_features':['sqrt','log2']},
        
                "KNeighborsClassifier":{'n_neighbors' : [5,7,9,11,13,15],
               'weights' : ['uniform','distance'],
               'metric' : ['minkowski','euclidean','manhattan']},
        
                "LogisticRegression":{}
                                            }
            
            score_dict=model_training(param=param,models=models,x_train_array=x_train_array,y_train_array=y_train_array,x_test_array=x_test_array,y_test_array=y_test_array)
            best_model_name=max(list(score_dict))
            best_model_score=score_dict[best_model_name]
            best_model=models[best_model_name]
            logging.info(f"Best model has been found and best model is {best_model_name } with test accuracy of {best_model_score}")
            # print(f"This is the best model {best_model} and it has the score of { best_model_score}")
            save_object(best_model,self.model_saving_path.model_path)
            logging.info("model has been save successfully")
            
        except Exception as e:
            raise CustomException(e)