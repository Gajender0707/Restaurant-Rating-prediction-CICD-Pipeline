import os
import dill
from logger import logging
from exception import CustomException


def save_object(obj,obj_path):
    try:
        with open(obj_path,"wb") as f:
            logging.info(f"{obj} will the save the object in {obj_path} path..")
            dill.dump(obj,f)
    except Exception as e:
        raise CustomException(e)