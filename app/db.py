from pymongo import MongoClient
import os

uri = os.environ.get("DATABASE_URI")

cliente = MongoClient(uri)

db = cliente[os.environ.get("DB_NAME")]