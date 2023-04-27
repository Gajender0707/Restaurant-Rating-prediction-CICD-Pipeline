
import logging
from datetime import datetime
import os

log_folder=os.path.join(os.getcwd(),"LOGS")
# print(log_folder)
sub_folder_name=datetime.now().strftime('%H_%M_%S_%d_%m_%y')
# print(sub_folder_name)
sub_folder_path=os.path.join(log_folder,sub_folder_name)
# print(sub_folder_path)
file_name=f"{datetime.now().strftime('%H_%M_%S_%d_%m_%y')}.log"
# print(file_name)
os.makedirs(sub_folder_path,exist_ok=True)
log_file_path=os.path.join(sub_folder_path,file_name)
# print(log_file_path)



logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s-%(lineno)s- %(message)s",

)

# logging.info("Hey")