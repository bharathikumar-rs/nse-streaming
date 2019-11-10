@echo off

echo starting zookeeper server
START "ZOOKEEPER" "zkserver"

timeout 30

echo starting Kafka server
START "KAFKA" "D:\servers\kafka_2.12\bin\windows\kafka-server-start.bat" d:\servers\kafka_2.12\config\server.properties

