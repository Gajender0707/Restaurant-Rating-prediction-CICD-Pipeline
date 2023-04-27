import os
import dill
from logger import logging
from exception import CustomException
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV


def save_object(obj,obj_path):
    try:
        with open(obj_path,"wb") as f:
            logging.info(f"{obj} will the save the object in {obj_path} path..")
            dill.dump(obj,f)
    except Exception as e:
        raise CustomException(e)
    

def load_object(object_path):
    try:
        with open(object_path,"rb") as f:
            logging.info(f"object is loading from the this path {object_path}")
            return dill.load(f)
    except Exception as e:
        raise CustomException(e)

def model_training(param,models,x_train_array,y_train_array,x_test_array,y_test_array):
    try:
        score_dict={}
        for i in range(len(list(models))):
            model_name=list(models.keys())[i]
            model=list(models.values())[i]
            para=param[model_name]
            rf_model=RandomizedSearchCV(model,para,cv=5)
            rf_model.fit(x_train_array,y_train_array)
            model.set_params(**rf_model.best_params_)
            model.fit(x_train_array,y_train_array)
            y_pred=model.predict(x_test_array)
            model_score=accuracy_score(y_pred,y_test_array)
            score_dict[model_name]=model_score
        return score_dict
    except Exception as e:
        raise CustomException(e)
    

    