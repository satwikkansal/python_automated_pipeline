from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def compute_product(a, b):
    product=a*b
    return product

if __name__ == "__main__":
    app.run()
