import os

from pymongo import MongoClient
from pymongo.server_api import ServerApi

class DB:
    def __init__(self):
        # MongoDB connection
        connection_uri = os.getenv('DATABASE_URL')
        db_name = os.getenv('MONGO_DB_NAME', 'tnp_db')
        client = MongoClient(connection_uri, server_api=ServerApi('1'))
        self.db = client[db_name]

        # Ping MongoDB to check connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as ex:
            print(f"Could not connect to MongoDB: {ex}")
        
db=DB().db
