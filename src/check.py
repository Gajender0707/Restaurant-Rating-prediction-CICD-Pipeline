from exception import CustomException
import mysql.connector as connection
import pandas as pd
import numpy as np
import dill
# try:
#     mydb = connection.connect(host="localhost", database = 'zomato',user="root", passwd="Gajender@123",use_pure=True)
#     query = "select online_order,book_table,rate,votes,rest_type,cost,type,city from zomato.zomato_5k;"
#     result_dataFrame = pd.read_sql(query,mydb)
#     mydb.close() #close the connection
# except Exception as e:
#     raise CustomException(e)

# print(result_dataFrame.head())
# print(type(result_dataFrame))
# print(result_dataFrame.shape)

# d={"Akash":29,"Rahul":3,"sanju":100,"umesh":200}
# # print(d["name"])
# best_model_name=max(d)
# print(best_model_name)
# print(f"best score: {d[best_model_name]}")
d1=np.array(["Yes","Yes",775,"Casual Dining" ,800,"Buffet","Banashankari"]).reshape(1,-1)
column_name=["online_order","book_table","votes","rest_type","cost","type","city"]

df1=pd.DataFrame(d1,columns=column_name)
print(df1)

with open(r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Restaurant-Rating-Prediction\Artifacts\model.pkl","rb") as f:
    m=dill.load(f)
print(m)
with open(r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Restaurant-Rating-Prediction\Artifacts\Preprocessor.pkl","rb") as f:
    p=dill.load(f)
print(p)

df_arr=p.transform(df1).toarray()
print(df_arr)

print(m.predict(df_arr))