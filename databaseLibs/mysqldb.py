import mysql.connector
import datetime
import loggerHelper
import json

client = None

def connect():
    global client
    try:
        client = mysql.connector.connect(host="mysqldb", database="MyTData")
    except:
        loggerHelper.getLogger().info("Error Connecting to MySQL")

    if client is None:
        loggerHelper.getLogger().info("Error Connecting to MySQL")


def writeData(body):
    global client
    data=body["data"]
    date=datetime.datetime.now()
    varnames = ""
    formatting = ""
    vals = ()
    for key, value in data.items():
        varnames = varnames + key + ","
        formatting = formatting + "%s,"
        vals = vals + (value,)
    varnames = varnames[:-1]
    formatting = formatting[:-1]
    loggerHelper.getLogger().info(varnames)
    loggerHelper.getLogger().info(vals)

    command = "INSERT INTO SensorData (" + varnames + ") VALUES (" + formatting + ")"
    loggerHelper.getLogger().info(command)

    client.cursor.execute(command, vals)

    client.commit()
