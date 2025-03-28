from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

from src.settings.config import settings


class MongoDBService:
    def __init__(self, uri: str, database_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[database_name]

        self.__setup

    @property
    def __setup(self):
        if 'users' not in self.db.list_collection_names():
            try:
                self.db.create_collection('users')
            except CollectionInvalid:
                pass

        if 'channels' not in self.db.list_collection_names():
            try:
                self.db.create_collection('channels')
            except CollectionInvalid:
                pass

    def add_document(self, collection_name: str, document: dict):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    def update_document(self, collection_name: str, query: dict, update: dict):
        collection = self.db[collection_name]
        result = collection.update_one(query, {"$set": update})
        return result.modified_count

    def delete_document(self, collection_name: str, query: dict):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count

    def get_all_documents(self, collection_name: str, param: dict = None):
        collection = self.db[collection_name]
        documents = collection.find(param) if param else collection.find()
        return list(documents)


db_service = MongoDBService(
    uri=settings.MONGO_URL,
    database_name=settings.MONGO_DB
)
