from __future__ import print_function
from __future__ import absolute_import
from pyspark import SparkConf, SparkContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from decimal import Decimal
from pyspark_cassandra import CassandraSparkContext, streaming
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='10.0.1.120:9092,10.0.1.86:9092,10.0.1.16:9092')

def handler(message, topic):
    records = message.collect()
    for record in records:
        producer.send(topic, json.dumps(record))
        producer.flush()

def main():
    conf = SparkConf().setAppName("Spark Cassandra").set("spark.cassandra.connection.host", "10.0.1.185,10.0.1.206")
    sc = CassandraSparkContext(conf=conf)
    ssc = StreamingContext(sc, 20)
    topic = 'iot-data-sensor'

    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": '10.0.1.120:9092,10.0.1.86:9092,10.0.1.16:9092'})
    ssc.checkpoint("./checkpoint")
    kvs = kvs.checkpoint(30)

    jsonRDD = kvs.map(lambda x: json.loads(x[1]))
    jsonRDD.pprint()

    nilai_avg = jsonRDD.map(lambda x: (x['waktu'], (x['suhu'], x['kelembapan'], x['ph'], 1))).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3])) \
        .map(lambda x: (x[0], float(x[1][0]) / x[1][3], float(x[1][1]) / x[1][3], float(x[1][2]) / x[1][3]))
    nilai_avg.foreachRDD(lambda x: handler(x, 'avg'))
    nilai_avg.pprint()
    nilai_avg.saveToCassandra("sensordb", "avg")

    nilai_max = jsonRDD.map(lambda x: (x['waktu'], (x['suhu'], x['kelembapan'], x['ph']))).reduceByKey(lambda x, y: max(x, y)).map(lambda x: (x[0], x[1][0], x[1][1], x[1][2])).transform(lambda x: x.sortBy(lambda a: a[0]))
    nilai_max.pprint()
    nilai_max.foreachRDD(lambda x: handler(x, 'max'))
    nilai_max.saveToCassandra("sensordb", "max")

    nilai_min = jsonRDD.map(lambda x: (x['waktu'], (x['suhu'], x['kelembapan'], x['ph']))).reduceByKey(lambda x, y: min(x, y)).map(lambda x: (x[0], x[1][0], x[1][1], x[1][2])).transform(lambda x: x.sortBy(lambda a: a[0]))
    nilai_min.pprint()
    nilai_min.foreachRDD(lambda x: handler(x, 'min'))
    nilai_min.saveToCassandra("sensordb", "min")

    ssc.start()
    ssc.awaitTermination()

if __name__ == "__main__":
    main()





