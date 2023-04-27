from logger import logging
from exception import CustomException
import os
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from utils import save_object
import numpy as np

@dataclass
class DataTransformationConfig:
        preprocessor_path=os.path.join("Artifacts","Preprocessor.pkl")
        logging.info("define the preprocessor path")

class DataTransformation:
        
        def __init__(self):
                self.preprocessor_path=DataTransformationConfig()
        
        def get_preprocessor(self):
                try:
                        num_features=['votes', 'cost']
                        cat_features=['online_order', 'book_table', 'rest_type', 'type', 'city']
                        logging.info("define the  numeric and categorical features")

                        num_pipeline=Pipeline(steps=[
                                ("imputing",SimpleImputer(strategy="mean")),
                                ("Scaling",StandardScaler())
                        ])

                        cat_pipeline=Pipeline(steps=[
                                ("Imputing",SimpleImputer(strategy="most_frequent")),
                                ("Encoding",OneHotEncoder())
                        ])
                        logging.info("Define the numeric and categorical pipelines")

                        Preprocessor=ColumnTransformer([
                                ("num_features",num_pipeline,num_features),
                                ("cat_features",cat_pipeline,cat_features)
                        ])
                        logging.info("define the preprocessor")
                        # print(Preprocessor)
                        return Preprocessor

                        
                except Exception as e:
                        raise CustomException(e)
                

        def Intiate_data_transformation(self,train_data_path,test_data_path):
            try:
                        train_data=pd.read_csv(train_data_path)
                        test_data=pd.read_csv(test_data_path)
                        Target="rate"
                        y=train_data[Target]
                        x=train_data.drop(Target,axis=1)
                        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
                        preprocessor=self.get_preprocessor()
                        logging.info("fetch the prerocessor Successfully.")
                        preprocessor.fit(x_train)
                        save_object(preprocessor,self.preprocessor_path.preprocessor_path)
                        logging.info("save the object successfully")

                        x_train_array=preprocessor.transform(x_train).toarray()
                        y_train_array=np.array(y_train).reshape(1,-1)
                        x_test_array=preprocessor.transform(x_test).toarray()
                        y_test_array=np.array(y_test).reshape(1,-1)

                        # print(x_train_array)
                        # print(x_train_array.shape)
                        # print(x_test_array.shape)
                        return (x_train_array,y_train_array,x_test_array,y_test_array)

                        
            except Exception as e:
                    raise CustomException(e)

# data_transformation_obj=DataTransformation()
# data_transformation_obj.get_preprocessor()
# data_transformation_obj.Intiate_data_transformation(r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Restaurant-Rating-Prediction\Artifacts\train.csv",
#                                          r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Restaurant-Rating-Prediction\Artifacts\test.csv")
        