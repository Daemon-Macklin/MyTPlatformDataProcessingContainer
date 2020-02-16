from pymongo import MongoClient
from datetime import datetime
import loggerHelper
import json

client = None

def connect():
    try:
        global client
        client = MongoClient('mongodb', 27017)

    except:
        loggerHelper.getLogger().info("Error Connecting to MongoDB")

    if client is None:
        loggerHelper.getLogger().info("Error Connecting to MongoDB")

def writeData(body):
    
    global client
    db = client["MyTData"]
    col = db[body["measurement"]]

    json_body = {
            "device" : body["sensor"],
            "date" : datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "data": body["data"]
    }

    loggerHelper.getLogger().info("Inserting Data:" + str(json_body))
    col.insert_one(json_body)

