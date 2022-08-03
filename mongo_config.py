from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
my_db = myclient["Dockerdb"]
my_collection = my_db["my_col"]