from flask import Blueprint, jsonify
import requests

class API:
    #Konstruktor
    def __init__(self,name= "blueprint_api", url_prefix = "/api"):
        self.__blueprint = Blueprint(name, __name__, url_prefix=url_prefix)
        self.__base__url = "https://fakestoreapi.com"
        self.__timeout = 5
        self.register_routes()

    def register_routes(self):
        @self.__blueprint.route("/products")
        def api_products():
            return jsonify(self.get_products())
        
    def get_products(self):
        response = requests.get(f"{self.__base__url}/products",timeout=self.__timeout)
        return response.json()
    
    def get_product(self, product_id):
        response = requests.get(f"{self.__base__url}/products/{product_id}",timeout=self.__timeout)
        return response.json()
    
    @property
    def blueprint(self):
        return self.__blueprint
    
