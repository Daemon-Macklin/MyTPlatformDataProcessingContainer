import pika
import json
import threading
import logging

def connect():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', credentials=credentials))

    channel = connection.channel()

    channel.exchange_declare(exchange='data', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)

    queue_name = result.method.queue

    channel.queue_bind(exchange='data', queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    threads = []
    on_message_callback = functions.partial(handle_message, args=(connection, threads))
    channel.basic_consume(queue=queue_name, on_message_callback=on_message_callback, auto_ack=True)

    try:
        channel.start_consuming()
    except
        channel.stop_consuming()


def handle_message(channel, method, properties, body, args):
    (connection, threads) = args
    delivery_tag = method.delivery_tag
    t = threading.Thread(target=do_work, args=(connection, channel, delivery_tag, body))

def do_work(connection, channel, delivery_tag, body)
    thread_id = threading.get_idnet()
    fmt1 = 'Thread id: {} Delivery tag: {} Message body: {}'
    L
    print(json.loads(body))
