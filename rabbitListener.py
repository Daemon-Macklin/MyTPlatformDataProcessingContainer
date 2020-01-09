import pika
import json
import threading
import logging
import functools
import time

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')

LOGGER = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def connect():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', credentials=credentials))

    channel = connection.channel()

    channel.exchange_declare(exchange='data', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)

    queue_name = result.method.queue
    print(queue_name)

    channel.queue_bind(exchange='data', queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    threads = []
    on_message_callback = functools.partial(handle_message, args=(connection, threads))
    channel.basic_consume(queue=queue_name, on_message_callback=on_message_callback)

    try:
        channel.start_consuming()
    except:
        channel.stop_consuming()

    # Wait for all to complete
    for thread in threads:
        thread.join()

    connection.close()


def handle_message(channel, method, properties, body, args):
    (connection, threads) = args
    delivery_tag = method.delivery_tag
    t = threading.Thread(target=do_work, args=(connection, channel, delivery_tag, body))
    t.start()
    threads.append(t)

def do_work(connection, channel, delivery_tag, body):
    thread_id = threading.get_ident()
    fmt1 = 'Thread id: {} Delivery tag: {} Message body: {}'
    LOGGER.info(fmt1.format(thread_id, delivery_tag, body))
    time.sleep(5)
    cb = functools.partial(ack_message, channel, delivery_tag)
    connection.add_callback_threadsafe(cb)

def ack_message(channel, delivery_tag):
    if channel.is_open:
        channel.basic_ack(delivery_tag)
    else:
        # Channel is already closed, so we can't ACK this message;
        pass
