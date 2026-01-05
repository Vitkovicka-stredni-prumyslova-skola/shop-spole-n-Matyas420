from flask import Flask
from api import api
from products import product_view

app = Flask(__name__)
api_blueprint = api.API()
app.register_blueprint(api_blueprint.blueprint)

products_blueprint = product_view.ProductView(api_blueprint)
app.register_blueprint(products_blueprint.blueprint)


if __name__ == '__main__':
    app.run(debug=True)