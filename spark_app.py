from __future__ import print_function
from __future__ import absolute_import
from pyspark import SparkConf, SparkContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark_cassandra import CassandraSparkContext, streaming
from decimal import Decimal
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='172.31.19.194:9092')

def handler(message, topic):
    records = message.collect()
    for record in records:
        producer.send(topic, json.dumps(record))
        producer.flush()

def avgdata(data):
    nilai_avg = data.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) \
        .map(lambda x: (x[0], float(x[1][0]) / x[1][1])).transform(lambda x: x.sortBy(lambda a: a[0]))
    return nilai_avg

def maxdata(data):
    nilai_max = data.reduceByKey(lambda x, y: max(x,y)).transform(lambda x: x.sortBy(lambda a: a[0]))
    return nilai_max

def mindata(data):
    nilai_min = data.reduceByKey(lambda x, y: min(x,y)).transform(lambda x: x.sortBy(lambda a: a[0]))
    return nilai_min

def main():
    conf = SparkConf().setAppName("Spark Cassandra").set("spark.cassandra.connection.host", "172.31.20.66,172.31.21.245")
    sc = CassandraSparkContext(conf=conf)
    ssc = StreamingContext(sc, 20)
    topic = 'iot-data-sensor'

    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": '172.31.19.194:9092'})

    jsonRDD = kvs.map(lambda x: json.loads(x[1]))
    jsonRDD.pprint()
    jsonRDD.saveToCassandra("sensordb", "sensor")

    map_data_suhu = jsonRDD.map(lambda x: (x['waktu'], (x['suhu'], 1)))
    map_data_kelembapan = jsonRDD.map(lambda x: (x['waktu'], (x['kelembapan'], 1)))
    map_data_ph = jsonRDD.map(lambda x: (x['waktu'], (x['ph'], 1)))

    data_suhu = jsonRDD.map(lambda x: (x['waktu'], x['suhu']))
    data_kelembapan = jsonRDD.map(lambda x: (x['waktu'], x['kelembapan']))
    data_ph = jsonRDD.map(lambda x: (x['waktu'], x['ph']))

    # SUHU
    avgsuhu = avgdata(map_data_suhu)
    avgsuhu.pprint()
    avgsuhu.foreachRDD(lambda x: handler(x, 'avgsuhu'))
    avgsuhu.saveToCassandra("sensordb", "suhu")

    maxsuhu = maxdata(data_suhu)
    maxsuhu.pprint()
    maxsuhu.foreachRDD(lambda x: handler(x, 'maxsuhu'))
    save_maxsuhu = avgsuhu.map(lambda x: (x[1]))
    save_maxsuhu.saveToCassandra("sensordb", "suhu")

    minsuhu = mindata(data_suhu)
    minsuhu.pprint()
    minsuhu.foreachRDD(lambda x: handler(x, 'minsuhu'))
    save_minsuhu = avgsuhu.map(lambda x: (x[1]))
    #save_minsuhu.saveToCassandra("sensordb", "suhu")

    # KELEMBAPAN
    avgkelembapan = avgdata(map_data_kelembapan)
    avgkelembapan.pprint()
    avgkelembapan.foreachRDD(lambda x: handler(x, 'avgkelembapan'))
    #avgkelembapan.saveToCassandra("sensordb", "avgkelembapan")

    maxkelembapan = maxdata(data_kelembapan)
    maxkelembapan.pprint()
    maxkelembapan.foreachRDD(lambda x: handler(x, 'maxkelembapan'))
    #maxkelembapan.saveToCassandra("sensordb", "maxkelembapan")

    minkelembapan = mindata(data_kelembapan)
    minkelembapan.pprint()
    minkelembapan.foreachRDD(lambda x: handler(x, 'minkelembapan'))
    #minkelembapan.saveToCassandra("sensordb", "minkelembapan")

    # PH
    avgph = avgdata(map_data_ph)
    avgph.pprint()
    avgph.foreachRDD(lambda x: handler(x, 'avgph'))
    #avgph.saveToCassandra("sensordb", "avgph")

    maxph = maxdata(data_ph)
    maxph.pprint()
    maxph.foreachRDD(lambda x: handler(x, 'maxph'))
    #maxph.saveToCassandra("sensordb", "maxph")

    minph = mindata(data_ph)
    minph.pprint()
    minph.foreachRDD(lambda x: handler(x, 'minph'))
    #minph.saveToCassandra("sensordb", "minph")

    ssc.start()
    ssc.awaitTermination()

if __name__ == "__main__":
    main()



