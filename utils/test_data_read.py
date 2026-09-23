import json


def load_order_data():
    with open("test-data/order_data.json") as file:
        return json.load(file)
