import psycopg2
import datetime
import loggerHelper
import json

client = None

def connect():
    global client
    try:
        client = psycopg2.connect(host="timescaledb", user="postgres", password="postgres", database="mytdata")
    except Exception as e:
        loggerHelper.getLogger().info(e)
        loggerHelper.getLogger().info("Error Connecting to Timescale")

    if client is None:
        loggerHelper.getLogger().info("Error Connecting to Timescale")


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

    command = "INSERT INTO sensordata (" + varnames + ") VALUES (" + formatting + ")"
    loggerHelper.getLogger().info(command)

    client.cursor().execute(command, vals)

    client.commit()
