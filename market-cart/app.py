from flask import Flask, request

from client import Client

app = Flask(__name__)


@app.route('/cart')
def cart():
    new_cart = request.args.get('new').encode().split(',')

    client = Client()
    client.add_items(new_cart)

    return '${0:.2f}\n'.format(client.get_total())


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
