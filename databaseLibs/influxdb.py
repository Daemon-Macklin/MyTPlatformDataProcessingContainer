from influxdb import InfluxDBClient
import datetime
import loggerHelper
import json
import pprint

client = None

def connect():
    try:
        global client
        client = InfluxDBClient(host='influxdb', port=8086, database="MyTData")
        loggerHelper.getLogger().info("Connected to InfluxDB")
    except:
        loggerHelper.getLogger().info("Error Connecting to InfluxDB")

def writeData(body):
    global client
    json_body = [
    {
        "measurement": body["measurement"],
        "tags": {
            "device": body["sensor"],
        },
        "time": datetime.now(),
        "fields": {
        }
    }
    ]

    json_body[0]["fields"] = body["data"]
    loggerHelper.getLogger().info("Inserting Data:" + str(json_body))
    client.write_points(json_body)
