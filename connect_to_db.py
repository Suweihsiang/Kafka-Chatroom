from pymongo import MongoClient
from pymongo.collection import Collection

def connect_to_mongodb(link: str, db: str, collection: str) -> Collection:
    """
    建立MongoDB連線，並取得指定之collection
    參數:
    - link(str):連線至MongoDB的URI(host及port)
    - db(str):資料庫名稱
    - collection(str):集合名稱
    回傳:
    - pymongo.collection.Collection:指定的MongoDB collection物件
    """
    mongo_client = MongoClient(link)
    mongo_db = mongo_client[db]
    mongo_collection = mongo_db[collection]
    return mongo_collection