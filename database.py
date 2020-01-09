from influxdb import InfluxDBClient
from datetime import datetime
import loggerHelper
import json
import pprint

client = None

def connect():
    try:
        global client
        client = InfluxDBClient(host='localhost', port=8086, database="MyTData")
        loggerHelper.getLogger().info("Connected to InfluxDB")
    except:
        loggerHelper.getLogger().info("Error Connecting to InfluxDB")

def writeData(body):
    global client
    body = json.loads(body)
    json_body = [
    {
        "measurement": body["measurement"],
        "tags": {
            "device": body["sensor"],
        },
        "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "fields": {
        }
    }
    ]

    json_body[0]["fields"] = body["data"]
    loggerHelper.getLogger().info("Inserting Data:" + str(json_body))
    client.write_points(json_body)
