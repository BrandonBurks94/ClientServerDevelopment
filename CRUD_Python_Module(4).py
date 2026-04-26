from pymongo import MongoClient


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        # Connection variables
        USER = "aacuser"
        PASS = "Brandon1994!"
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d/%s' % (USER, PASS, HOST, PORT, DB))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a document into the animals collection"""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Create failed:", e)
                return False
        else:
            print("Create failed: data parameter is empty")
            return False

    def read(self, query):
        """Query documents from the animals collection"""
        if query is not None:
            try:
                result = self.collection.find(query, {"_id": False})
                return list(result)
            except Exception as e:
                print("Read failed:", e)
                return []
        else:
            print("Read failed: query parameter is empty")
            return []

    def update(self, query, new_values):
        """Update document(s) in the animals collection"""
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print("Update failed:", e)
                return 0
        else:
            print("Update failed: query or new_values parameter is empty")
            return 0

    def delete(self, query):
        """Delete document(s) from the animals collection"""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Delete failed:", e)
                return 0
        else:
            print("Delete failed: query parameter is empty")
            return 0