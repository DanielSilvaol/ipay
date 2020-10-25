from pymongo import MongoClient


class SalesRepository:

    __cluster = MongoClient("mongodb+srv://admin:loba@loba.jbtnz.mongodb.net/loba?retryWrites=true&w=majority")
    __db = __cluster["loba"]
    __sale_collection = __db["sale"]

    def find_all(self):
        return self.__sale_collection.find()

    def find_by_product_name(self, product_name):
        return self.__sale_collection.find({'name': product_name})


