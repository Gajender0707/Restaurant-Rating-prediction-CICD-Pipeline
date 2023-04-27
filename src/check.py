from exception import CustomException
import mysql.connector as connection
import pandas as pd
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

d={"Akash":29,"Rahul":3,"sanju":100,"umesh":200}
# print(d["name"])
best_model_name=max(d)
print(best_model_name)
print(f"best score: {d[best_model_name]}")

