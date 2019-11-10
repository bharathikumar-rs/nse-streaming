# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:07:06 2019

@author: ArchuBharathi
"""

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='NSE_NEW')
channel.queue_delete(queue='NSE_NEW')
channel.close()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='NSE_NEW', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


