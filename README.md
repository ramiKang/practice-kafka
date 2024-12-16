# Kafka를 활용한 Streaming Data Algorithm 구현

* Streaming Data 기말 프로젝트로 Kafka를 활용한 간단하게 streaming data algorithm 구현

## 구현 알고리즘
* Count-Min Sketch
* Sliding Window Protocol

## 실행 방법
아래의 과정을 따라 실행

**1. Kafka 다운로드**
* 아래 링크에서 Binary Downloads (.tgz)
* Scala v2.13 | Kafka v3.9.0 (2024.12.16일 기준)
* https://kafka.apache.org/downloads

**2. tar 해제**

    tar -xzf kafka_2.13-3.9.0.tgz

**3. 권한 수정**

    chmod -R +x ./bin

**4. shell 실행**

본 코드는 kafka 디렉토리가서 실행할 것
    
    # Zookeeper 실행
    ./bin/zookeeper-server-start.sh ./config/zookeeper.properties
    
    # Kafka 실행
    ./bin/kafka-server-start.sh ./config/server.properties
  
**5. 코드 실행**

    # Producer
    python3 stream_data_to_kafka.py
    
    # Consumer
    python3 consume_and_process.py
