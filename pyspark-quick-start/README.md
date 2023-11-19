# PySpark Quick Start

<br />

## List of Contents:

### 1. [Quick Start](#content-1)

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





**[⬆ back to top](#list-of-contents)**

<br />

---

## References:
- https://spark.apache.org/docs/latest/quick-start.html
- 
