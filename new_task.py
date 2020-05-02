

# import pika

# connection = pika.BlockingConnection(pika.ConnectionParameters(
#     host='localhost'))
# channel = connection.channel()

# channel.queue_declare(queue='hello')


# channel.basic_publish(exchange='',
#                     routing_key='hello',
#                     body='hello world!')
# print('[x] sent "hello world!"')

# connection.close()

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')


message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message.encode('utf-8'))

print(f"[x] Sent {message}")
connection.close()

