#!/usr/bin/env python3

import sys
import json
import random
import time
from datetime import datetime
import paho.mqtt.client as mqtt
import uuid

def generate(host, port, username, password, topic, sensors, interval_ms, verbose):

    mqttc = mqtt.Client()

    if username:
        mqttc.username_pw_set(username, password)

    mqttc.connect(host, port)

    keys = list(sensors.keys())
    interval_secs = interval_ms / 1000.0 # 1 detik

#generate data terus menerus, dengan 10 message per detik
    while True:
        for counter in range(1000):
            id = str(uuid.uuid4())
            sensor_id = random.choice(keys)
            sensor = sensors[sensor_id]

            # Temperatur
            min_valtemp, max_valtemp = sensor.get("suhu", [20, 30])
            valtemp = random.randint(min_valtemp, max_valtemp)

            # Humidity
            min_valhum, max_valhum = sensor.get("kelembapan", [36, 50])
            valhum = random.randint(min_valhum, max_valhum)

            # pH
            min_valph, max_valph = sensor.get("ph", [5.8, 7.8])
            valph = round(random.uniform(min_valph, max_valph), 1)

            waktu = datetime.now()
            data = {
                "id": id,
                "sensor": sensor_id,
                "suhu": valtemp, "kelembapan": valhum, "ph": valph, "waktu": waktu.strftime("%Y-%m-%d %H:%M:%S")
            }
            payload = json.dumps(data)

            print("%s%s: %s" % (topic, counter, payload))
            mqttc.publish(topic, payload)

        time.sleep(interval_secs)

def main(config_path):
    """main, load isi dari config.json dan memanggil function generate"""
    try:
        with open(config_path) as handle:
            config = json.load(handle)
            mqtt_config = config.get("mqtt", {})
            misc_config = config.get("misc", {})
            sensors = config.get("sensors")

            interval_ms = misc_config.get("interval_ms", 500)
            verbose = misc_config.get("verbose", False)

            if not sensors:
                print("no sensors specified in config, nothing to do")
                return

            host = mqtt_config.get("host", "172.31.81.182")
            port = mqtt_config.get("port", 1883)
            username = mqtt_config.get("username")
            password = mqtt_config.get("password")
            topic = mqtt_config.get("topic", "sensors")

            dateTimeObj = datetime.now()
            timeObj = dateTimeObj.time()
            time.sleep(1 - (timeObj.microsecond / 1000000))

            generate(host, port, username, password, topic, sensors, interval_ms, verbose)
    except IOError as error:
        print("Error opening config file '%s'" % config_path, error)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("usage %s config.json" % sys.argv[0])