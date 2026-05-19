import argparse
import json
import uuid

from confluent_kafka import Producer


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", type=str, help="user name")
    parser.add_argument("-i", "--item", type=str, help="item name")
    parser.add_argument("-q", "--quantity", type=int, help="quantity")

    return parser.parse_args()


def create_order() -> dict:
    args = get_args()
    return {
        "order_id": str(uuid.uuid4()),
        "user": args.user,
        "item": args.item,
        "quantity": args.quantity
    }


def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode("utf-8")}")
        print(f"✅ Delivered to {msg.topic()} | partition {msg.partition()} | offset {msg.offset()}")


def create_producer():
    producer_config = {
        "bootstrap.servers": "localhost:9092"
    }

    return Producer(producer_config)


def send_item(topic: str, order: dict):
    producer = create_producer()
    try:
        producer.produce(
            topic=topic,
            value=json.dumps(order).encode("utf-8"),
            callback=delivery_report,
        )
    except Exception as err:
        print(f"❌ Delivery failed: {err}")
    finally:
        producer.flush()

def main():
    order = create_order()
    send_item("orders", order)

if __name__ == '__main__':
    main()