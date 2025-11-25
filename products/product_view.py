from flask import Blueprint, render_template

class ProductView:
    def __init__(self, api_instance, name="procuts", url_prefix="/products"):
        self.__api = api_instance #Propojení s API
        self.__blueprint = Blueprint(name, __name__, url_prefix=url_prefix, template_folder="products/templates")
        self._register_routes()

    def __register_routes(self):
        @self.blueprint.route("/")
        def list_products():
            products = self.__api.get_products()
            return render_template("products.html", products = products)
        
        @self.blueprint.route("/<int:product_id>")
        def detail_products(product_id):
            product = self.__api.get_product(product_id)
            return render_template("detail_product.html", product = product)

    @property
    def blueprint(self):
        return self.__blueprint