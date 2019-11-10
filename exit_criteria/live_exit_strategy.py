from kafka import KafkaConsumer
import json
from kafka.errors import KafkaError
import pandas as pd
from exit_criteria.nse_json_parser import nse_json_parser
from kafka import KafkaProducer
import logging
from logging.config import fileConfig

class live_exit_strategy:
# =============================================================================
#
#  Kakfa Topic conusmer program
#  will keep on running until a keyboard intreput or unhandled exception thrown
#  wirte the decision strategy for each stock to NSE_sell topic
# =============================================================================
    def __init__(self):

        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')

        self.consumer = KafkaConsumer('NSE_NEW'
                                      ,bootstrap_servers=['localhost:9092']
                                      ,auto_offset_reset='latest'
                                      ,enable_auto_commit=True
                                     # ,auto_commit_interval_ms=1000
                                      ,group_id='NSE-group'
                                      ,value_deserializer=
                                      lambda m: json.loads(m.decode('utf-8')))

        self.connection = KafkaProducer(bootstrap_servers='localhost:9092'
                                        ,value_serializer=
                                        lambda v:json.dumps(v).encode('utf-8'))

    # consumer = KafkaConsumer('NSE_NEW')
    def consume_topic(self):

# =============================================================================
#         Consume the message from defined topic "NSE_NEW",in realtime
#         parse the json
#         check agains the purchased stocks and  make a decision
# =============================================================================
        for message in self.consumer:
            parse = nse_json_parser()
            parse.json_to_df_yahoo(message.value, self.connection)
            del parse

def main():
    live  = live_exit_strategy()
    print("Kafka consumer started for topic NSE_NEW !!!!!!!!!!!!!")
    live.consume_topic()


if __name__ == "__main__":
    main()