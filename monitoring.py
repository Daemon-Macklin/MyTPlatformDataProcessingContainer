import psutil
import pika
import json
import configparser


def diskMonitoring():

    disks = psutil.disk_partitions()

    dbPath = "/var/lib/mytDatabase"
    rootPath = "/"

    for disk in disks:
        if disk.mountpoint == dbPath:
            db = psutil.disk_usage(disk.mountpoint).percent
        elif disk.mountpoint == rootPath:
            root = psutil.disk_usage(disk.mountpoint).percent
   
    return db, root

def data():
    
    db, root = diskMonitoring()
    json_body = {
        "measurement": "SystemMonitoring",
        "sensor": "platform",
        "data": {
            "dbDisk" : db,
            "rootDisk" : root,
            "cpu" : psutil.cpu_percent(),
            "virRam" : psutil.virtual_memory().percent,
            "swapRam" : psutil.swap_memory().percent
            }
        }
    
    return json.dumps(json_body, sort_keys=True)

def main():
    conf = configparser.ConfigParser()
    conf.read("config.ini")
    user = conf["rabbitmq"]["user"]
    password = conf["rabbitmq"]["password"]
    tls = conf["rabbitmq"]["tlsenabled"]
    
    if user == "" or password == "":
        if tls == "false":
            connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        else:
            context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            context.load_verify_locations("cert_rabbitmq/cacert.pem")
            context.load_cert_chain(certfile="cert_rabbitmq/cert.pem", keyfile="cert_rabbitmq/key.pem")

            ssl_options = pika.SSLOptions(context)

            connection = pika.BlockingConnection(pika.ConnectionParameters(
                    host="localhost", port=5671, ssl_options=ssl_options))
    else:
        credentials = pika.PlainCredentials(user, password)
        if tls == "false":
            connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', credentials=credentials))
        else:
            context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            context.load_verify_locations("cert_rabbitmq/cacert.pem")
            context.load_cert_chain(certfile="cert_rabbitmq/cert.pem", keyfile="cert_rabbitmq/key.pem")

            ssl_options = pika.SSLOptions(context)

            connection = pika.BlockingConnection(pika.ConnectionParameters(
                    host="34.244.187.201", port=5671, ssl_options=ssl_options))

    channel = connection.channel()
    
    channel.exchange_declare(exchange='data', exchange_type='fanout')

    message = data() 
    # message = json.loads(message)
    print(message)
    channel.basic_publish(exchange='data', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    connection.close()

main()    


