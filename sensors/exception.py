import sys
import os


def error_message_details(error, error_detail:sys):
    _,_,exc_tb = sys.error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "ERROR OCCURED IN PYTHON SCRIPT name [{0}] line number [{1}] error message [{2}]".format(
        filename, exc_tb.tb_lineno, str(error)  # Use line number and error message
    )
    return error_message


class CustomException(Exception):
    def __init__(self , error_message , error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message , error_detail=error_detail)
        
        
    def __str__(self):
        return self.error_message
    
            
        