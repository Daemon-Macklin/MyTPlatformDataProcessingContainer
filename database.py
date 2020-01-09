from influxdb import InfluxDBClient
import time

client = None

def connect():
    try:
        client = InfluxDBClient(host='localhost', port=8086)
    except:
        print("DB Error")

def writeData():
    print("Write")
