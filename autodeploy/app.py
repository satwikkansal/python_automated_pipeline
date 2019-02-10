from __future__ import division
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/division')
def get_division():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    return str(compute_division(x,y))

def compute_division(x, y):
    if y == 0:
        return float('inf')
    return x/y
