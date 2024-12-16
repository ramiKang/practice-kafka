from kafka import KafkaConsumer
import json
from count_sketch import CountSketch
from slidingWindow import SlidingWindow
from constants import TOPIC_NAME,KAFKA_SERVER_HOST

# Kafka Consumer 생성
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_SERVER_HOST,
    api_version=(0,11,5),
    value_deserializer=lambda v: json.loads(v)
)

# Sliding Window
sliding_window = SlidingWindow(window_size=30)

# Count Sketch
cs = CountSketch(width=200, depth=5)


# 메시지 한 개씩 처리
for message in consumer:
    data = message.value
    country = data.get('country', 'unknown')
    cs.update(str(country), 1)

    sliding_window.add_event(country)
    current_events = sliding_window.get_events()

    country_count = {}
    for loc in current_events:
        country_count[loc] = country_count.get(loc, 0) + 1

    print(f"\n{'='*30}")
    print(f"[Current Country Count] country: {country}, Estimated Frequency: {cs.estimate(str(country))}")
    print(f"[Sliding Window Country Frequency] : {country_count}")
    print(f"\n{'='*30}")

