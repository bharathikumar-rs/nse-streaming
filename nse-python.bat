@echo off

@echo off

echo starting zookeeper server
START "ZOOKEEPER" "zkserver"

START "ZOOKEEPER" "D:\servers\kafka_2.3.1\bin\windows\zookeeper-server-start.bat" d:\servers\kafka_2.3.1\config\zookeeper.properties

timeout 20

echo starting Kafka server
#START "KAFKA" "D:\servers\kafka_2.12\bin\windows\kafka-server-start.bat" d:\servers\kafka_2.12\config\server.properties
START "KAFKA" "D:\servers\kafka_2.3.1\bin\windows\kafka-server-start.bat" d:\servers\kafka_2.3.1\config\server.properties


timeout 30


echo starting Kafka produce and consumer
echo "--------------------------------------"

echo starting Kafka producer
echo "--------------------------------------"
start cmd.exe /k  cd "scheduler" ^& python nseschedule.py


timeout 10

echo starting Kafka Consumer
echo "--------------------------------------"
start cmd.exe /k  cd "exit_criteria" ^& python live_exit_strategy.py

echo "All tasks started successfully!!!!!!!!!"


START "KAFKATopic" "D:\servers\kafka_2.3.1\bin\windows\kafka-topics.bat" --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 10 --topic NSE_NEW

exit






