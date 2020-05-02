import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    body = body.decode('utf-8')
    print(f"[x] Received {body}")
    time.sleep(body.count('.'))
    print("Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_consume('hello',
                      callback,
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()