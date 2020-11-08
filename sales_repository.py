import os

from pymongo import MongoClient


# class SalesRepository:

    # __mongo_uri = os.getenv('MONGODB_URI')
    # print(__mongo_uri)
    #
    # __cluster = MongoClient("mongodb+srv://admin:loba@loba.jbtnz.mongodb.net/loba?retryWrites=true&w=majority")
    # __db = __cluster["loba"]
    # __sale_collection = __db["sale"]
    #
    # def find_all(self):
    #     return self.__sale_collection.find()
    #
    # def find_by_product_name(self, product_name):
    #     return self.__sale_collection.find({"name": {"$regex": product_name, "$options": "i"}})
    #
    # def find_all_company(self):
    #     return self.__sale_collection.distinct('company')
    #
    # def find_plans_by_classification(self, classification):
    #     return self.__sale_collection.find({"classification": {"$regex": classification, "$options": "i"}})

