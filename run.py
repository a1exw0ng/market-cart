from flask import Flask, request

from client import Client

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/cart')
def cart(product_list=[]):
    new_cart = request.args.get('new').encode().split(',')

    client = Client()
    client.add_items(new_cart)

    return '$' + str(client.get_total())


if __name__ == '__main__':
    app.run()
