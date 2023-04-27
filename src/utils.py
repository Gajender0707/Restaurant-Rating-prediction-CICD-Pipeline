import os
import dill
from logger import logging
from exception import CustomException
from sklearn.metrics import accuracy_score


def save_object(obj,obj_path):
    try:
        with open(obj_path,"wb") as f:
            logging.info(f"{obj} will the save the object in {obj_path} path..")
            dill.dump(obj,f)
    except Exception as e:
        raise CustomException(e)
    

def model_training(models,x_train_array,y_train_array,x_test_array,y_test_array):
    try:
        score_dict={}
        for i in range(len(models)):
            model_name=list(models.keys())[i]
            model=list(models.values())[i]
            model.fit(x_train_array,y_train_array)
            # print(model)
            y_pred=model.predict(x_test_array)
            score=accuracy_score(y_pred,y_test_array)
            score_dict[model_name]=score
        
        return score_dict

            
    except Exception as e:
        raise CustomException(e)
    