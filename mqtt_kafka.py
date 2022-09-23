import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from kafka.errors import KafkaError, NoBrokersAvailable
import time
import os

## KAFKA
# Mengirim message ke kafka
def send_message_to_kafka(message):
    print("Mengirim message ke kafka: %s" % message)
    # Topik di kafka
    producer.send('iot-data-sensor', message)

## MQTT
# Callback ketika terkoneksi ke MQTT.
# rc : digunakan untuk check jika koneksi sudah ada/established
def on_connect(client, userdata, flags, rc):
    print("Connect %s, %s, %s %s" % (client, userdata, flags, rc))
    # Subscribe topik di MQTT.
    client.subscribe("sensors")

# Callback untuk disconnect event
def on_disconnect(client, user_data, rc):
    print("""Disconnect
    client: %s
    user_data: %s
    rc: %s
    """ % (client, user_data, rc))

# Callback ketika sebuah message di publish akan diterima
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    send_message_to_kafka(msg.payload)

def mqtt_to_kafka_run():
    # Mengambil message dari MQTT queue dan memasukkan ke kafka
    client_name = "home_connector_%s" % os.getenv("HOSTNAME")
    client = mqtt.Client(client_id=client_name)

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    #connect ke MQTT broker
    client.username_pw_set(username="fidia", password="12345678")
    client.connect("172.31.81.182", 1883, 60)
    client.loop_forever()

if __name__ == '__main__':
    attempts = 0

    while attempts < 10:
        try:
            brokers = os.getenv("KAFKA_HOSTS", "").split(",")
            producer = KafkaProducer(bootstrap_servers='172.31.90.3:9092,172.31.17.238:9092,172.31.95.169:9092')
            mqtt_to_kafka_run()

        # Catatan jika Kafka error
        except NoBrokersAvailable:
            print("Tidak ada broker kafka yang on %s" % attempts)
            attempts = attempts + 1
            time.sleep(2)