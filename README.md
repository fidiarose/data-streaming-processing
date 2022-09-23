# data-streaming-processing
My Undergraduate Thesis 
The Platform Development of the Distributed Processing for IoT Data Streams using Spark Streaming
Stream processing is becoming essential of IoT stack to increase the values and benefits for the organization. Stream processing requires data processing with high throughput, low latency and fault tolerance. Along with the growth in streaming data, centralized architecture will cause large delays for providing service. To solve this problem, additional resources or machines in the cluster are needed to maintain processing performance. It needs a system for distributed data processing. This research proposes to develop a distributed IoT data stream processing platform using Spark Streaming. 

The platform built consist of 4 components, such as data processing, data integration, storage and interface. 

The selection of these components is based on the availability and support of data source and data sinks on Spark Streaming.

Spark Streaming is able to provide distributed data processing and handle the throughput and latency well. Furthermore, the ability of Spark Streaming to use the distributed resources efficiently with the track the CPU and memory utilization across all the nodes that are being used by Spark Streaming user code. Additionally, Spark Streaming stable in handling recovery when a node fails. The performance test results showed, Spark Streaming can handle an increase in input data streaming to 2000 records every second and it can handle recovery when one of the workers fails.
