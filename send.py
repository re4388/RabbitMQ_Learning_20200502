

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

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()

