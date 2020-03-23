import mysql.connector
import datetime
import loggerHelper
import json

client = None

def connect():
    global client
    try:
        client = mysql.connector.connect(host="mysqldb", user="root", passwd="", database="MyTData")
    except Exception as e:
        loggerHelper.getLogger().info(e)
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
    varnames = varnames + "ts"
    formatting = formatting + "%s"
    vals = vals + (date,)
    loggerHelper.getLogger().info(varnames)
    loggerHelper.getLogger().info(vals)

    command = "INSERT INTO SensorData (" + varnames + ") VALUES (" + formatting + ")"
    loggerHelper.getLogger().info(command)

    client.cursor().execute(command, vals)

    client.commit()
