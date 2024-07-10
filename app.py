import random
from flask import Flask
from numpy.random import randint


app = Flask(__name__)

@app.route('/index')
def hello():
    return 'Hello'

@app.route('/moreload')
def moreload():
    array = randint(0, 100, 1000)
    sum_array = sum(array)
    return str(sum_array)

if __name__:
    app.run(host='0.0.0.0', port=int('5000'), debug=True)