from logger import logging
from exception import CustomException
import numpy as np
import pandas as pd
from utils import load_object

class Prediction:

    def __init__(self,online_order,book_table,votes,rest_type,cost,type,city):
        self.online_order=online_order
        self.book_table=book_table
        self.votes=votes
        self.rest_type=rest_type
        self.cost=cost
        self.type=type
        self.city=city
        logging.info("get all the data")

    def get_dataframe(self):
        try:

            data_points=[self.online_order,
                        self.book_table,
                        self.votes,
                        self.rest_type,
                        self.cost,
                        self.type,self.city]
            dp=np.array(data_points).reshape(1,-1)
            logging.info(f"get the data points and reshape them for fit the dataframe and data points are: {dp}")
            column_name=["online_order","book_table","votes","rest_type","cost","type","city"]
            input_df=pd.DataFrame(dp,columns=column_name)
            logging.info(f"Create the dataframe for the input of Model ")
            return input_df
        except Exception as e:
            raise CustomException(e)
    def Predict_rating(self,preprocessor_path,model_path):
        try:
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            new_df=self.get_dataframe()
            new_df_array=preprocessor.transform(new_df)
            predict=model.predict(new_df_array)
            return predict[0]
        except Exception as e:
            raise CustomException(e)
        


# prediction_obj=Prediction("Yes","Yes",775,"Casual Dining" ,800,"Buffet","Banashankari")
# preprocessor_path=r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Restaurant-Rating-Prediction\Artifacts\Preprocessor.pkl"
# model_path=r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Restaurant-Rating-Prediction\Artifacts\model.pkl"
# prediction_obj.Predict_rating(preprocessor_path=preprocessor_path,model_path=model_path)