# PySpark Tutorial

<br />

## List of Contents:

### 1. [Quick Start](#content-1)
### 2. [PySpark Tutorial for Beginners](#content-2)


<br />

---

## Contents:

## [Quick Start](https://spark.apache.org/docs/latest/quick-start.html) <span id="content-1"></span>

### Run PySpark in Docker (with Jupyter)
- Pull the image with `docker pull quay.io/jupyter/pyspark-notebook`
- Or have this docker-compose.yaml:
  ```text
  version: "3.7"
  
  services:
    pyspark:
      image: quay.io/jupyter/pyspark-notebook
      container_name: pyspark-quick-start
      environment:
        JUPYTER_ENABLE_LAB: "yes"
      ports:
        - "8888:8888"
      volumes:
        - ./:/home/jovyan/work
  ```


## [PySpark Tutorial For Beginners](https://sparkbyexamples.com/pyspark-tutorial/) <span id="content-2"></span>

### PySpark Tutorial Introduction
- PySpark is an Apache Spark library written in Python to run Python applications using Apache Spark capabilities. Using PySpark we can run applications parallelly on the distributed cluster (multiple nodes).

### What is Apache Spark?
- Apache Spark is an open-source unified analytics engine used for large-scale data processing, hereafter referred it as Spark.
- Spark is designed to be fast, flexible, and easy to use, making it a popular choice for processing large-scale data sets.
- Spark can run on single-node machines or multi-node machines(Cluster).
- It was created to address the limitations of MapReduce, by doing in-memory processing. Spark reuses data by using an in-memory cache to speed up machine learning algorithms that repeatedly call a function on the same dataset.

### What are the Features of PySpark?
- In-memory computation
- Distributed processing using parallelize
- Can be used with many cluster managers (Spark, Yarn, Mesos e.t.c)
- Fault-tolerant
- Immutable
- Lazy evaluation
- Cache & persistence
- Inbuild-optimization when using DataFrames
- Supports ANSI SQL

### Advantages of PySpark
- PySpark is a general-purpose, in-memory, distributed processing engine that allows you to process data efficiently in a distributed fashion.
- Applications running on PySpark are 100x faster than traditional systems.
- You will get great benefits from using PySpark for data ingestion pipelines.
- Using PySpark we can process data from Hadoop HDFS, AWS S3, and many file systems.
- PySpark also is used to process real-time data using Streaming and Kafka.
- Using PySpark streaming you can also stream files from the file system and also stream from the socket.
- PySpark natively has machine learning and graph libraries.

### PySpark Architecture
- Apache Spark works in a master-slave architecture where the master is called the “Driver” and slaves are called “Workers”.
- When you run a Spark application, Spark Driver creates a context that is an entry point to your application, and all operations (transformations and actions) are executed on worker nodes, and the resources are managed by Cluster Manager.
  ![PySpark Architecture](https://sparkbyexamples.com/ezoimgfmt/i0.wp.com/sparkbyexamples.com/wp-content/uploads/2020/02/spark-cluster-overview.png?w=596&ssl=1&ezimgfmt=ng:webp/ngcb1)

### PySpark Modules & Packages
- PySpark RDD (pyspark.RDD)
- PySpark DataFrame and SQL (pyspark.sql)
- PySpark Streaming (pyspark.streaming)
- PySpark MLib (pyspark.ml, pyspark.mllib)
- PySpark GraphFrames (GraphFrames)
- PySpark Resource (pyspark.resource) It’s new in PySpark 3.0
- Ecosystem:
  ![Ecosystem](https://sparkbyexamples.com/ezoimgfmt/i0.wp.com/sparkbyexamples.com/wp-content/uploads/2020/02/spark-components-1.jpg?w=1018&ssl=1&ezimgfmt=ng:webp/ngcb1)

**[⬆ back to top](#list-of-contents)**

<br />

---

## References:
- https://spark.apache.org/docs/latest/quick-start.html
- 
