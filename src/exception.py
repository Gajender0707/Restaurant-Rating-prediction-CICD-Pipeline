import sys
from logger import logging

def error_message_detail(e):
    exc_tb=sys.exc_info()[2]
    error=e
    lineno=exc_tb.tb_lineno
    logging.info("Lineno find")
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"""An error has been Occured in Python script and error is <<{e}>> on the line no
      <<{lineno} in the file <<{file_name}>>"""
    logging.info("Set the Error message .")
    return error_message

class CustomException(Exception):
    logging.info("Define the Customexception class using predefind class Exception.")
    def __init__(self,error):
        super().__init__(self,error)
        self.error=error_message_detail(error)

    def __str__(self):
        logging.info("Create the function to return the error message..")
        return self.error
    

# if __name__=="__main__":
#     try:
#         print(a+29)
#     except Exception as e:
#         raise CustomException(e)
