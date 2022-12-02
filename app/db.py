from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017/')

db=cliente['rick_y_morty']
