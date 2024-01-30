# logging with exception

import logging

logging.basicConfig(filename='log1.txt', level=logging.INFO)
logging.info("a new request came")

try :
    x= int(input("Enter first no : "))
    y= int(input("Enter second no : "))
    print(x/y)
except ZeroDivisionError as msg:
    print("can't divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("enter only int values")
    logging.exception(msg)
logging.info("Request processing completed")

