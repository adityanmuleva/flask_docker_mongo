from pymongo import MongoClient
import os

myclient = MongoClient("mongodb://localhost:27017/")
my_db = myclient["Dockerdb"]
my_collection = my_db["my_col"]

# client = MongoClient('example.com',
#                      username='user',
#                      password='password',
#                      authSource='the_database',
#                      authMechanism='SCRAM-SHA-256')

uri = os.environ["MONGO_DB_URI"]
# uri = "mongodb://user:password@example.com/?authSource=the_database&authMechanism=SCRAM-SHA-256"
client = MongoClient(uri)