import sys
from kafka import KafkaConsumer
import json
from cassandra.cluster import Cluster

consumer = KafkaConsumer('iot-data-sensor', bootstrap_servers="172.31.37.17:9092")
cluster = Cluster(['172.31.20.66','172.31.21.245'])
session = cluster.connect('sensordb')

# start the loop
try:
    for message in consumer:
        entry = json.loads(message.value)
        session.execute(
            """
INSERT INTO sensor (id, kelembapan, ph, sensor, suhu, waktu)
VALUES (%s, %s, %s, %s, %s, %s)
""",
            (entry['id'],
             entry['kelembapan'],
             entry['ph'],
             entry['sensor'],
             entry['suhu'],
             entry['waktu']))
except KeyboardInterrupt:
    sys.exit()
