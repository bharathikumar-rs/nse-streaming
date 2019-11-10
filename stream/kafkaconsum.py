from kafka import KafkaConsumer
import json
from kafka.errors import KafkaError
import pandas as pd
from exit_criteria.nse_json_parser import nse_json_parser
import pika
from pika.connection import ConnectionParameters
from pika import credentials as pika_credentials, BasicProperties
from pika.exceptions import AMQPError, ChannelClosed, ConnectionClosed
from kafka import KafkaProducer

#consumer = KafkaConsumer('NSE_NEW')
consumer = KafkaConsumer('NSE_NEW', bootstrap_servers=['localhost:9092'],
                          auto_offset_reset='latest', enable_auto_commit=True,
                          auto_commit_interval_ms=1000, group_id='NSE-group',
                          value_deserializer=lambda m: json.loads(m.decode('utf-8')))

lst=[]

connection = KafkaProducer(bootstrap_servers='localhost:9092'
                                        ,value_serializer=lambda v:json.dumps(v).encode('utf-8'))
for message in consumer:
    parse = nse_json_parser()
    parse.json_to_df(message.value,connection)
    del parse
    # print( type(message.value))
    #  print (message.value)
    """
        s = str(message.value).replace("\'", '"')
       s = s.replace("None",'\"''None''\"')
       s = s.replace("False",'\"''False''\"')
       ps = json.loads(s)
      # lst.append(ps)
       lst = [ps]

       #lst.clear()
    """