from flask import Flask
from housing.logger import logging
app = Flask(__name__)

@app.route('/' , methods=['POST' , 'GET'])
def index():
    logging.INFO('we are building logging file')
    return 'hello world'

if __name__=='__main__':
    app.run(debug=True)