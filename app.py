from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)


@app.route('/' , methods=['POST' , 'GET'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        housing=HousingException(e, sys)
        logging.info(housing.error_message)
        logging.info('we are building logging file')
    return 'hello world'

if __name__=='__main__':
    app.run(debug=True)