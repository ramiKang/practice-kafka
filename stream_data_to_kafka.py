from kafka import KafkaProducer
import json
import time
import random
from constants import TOPIC_NAME,KAFKA_SERVER_HOST

DATA_ROOT_PATH = "./data"
json_path = f"{DATA_ROOT_PATH}/shop_clothing_2008.json"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER_HOST,
    api_version=(0,11,5),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open(json_path) as f:
    for line in f:
        producer.send(TOPIC_NAME, json.loads(line))
        print(f"데이터 전송: {line.strip()}")
        delay = random.uniform(0.5, 1)
        time.sleep(1)  # 1초 간격으로 전송