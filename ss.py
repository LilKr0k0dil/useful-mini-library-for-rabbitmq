#!/usr/bin/env python
import pika, requests

def read_and_write(queue,host):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    def callback(ch, method, properties, body):
        return body

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    
    requests.post(url=f'http://localhost/api/wifi/brute/incoming/mes', data=callback, headers={'Content-Type': 'application/json'})
    
