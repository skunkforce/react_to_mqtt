import os
import uuid
from paho.mqtt import client as mqtt

action = os.getenv('REACT_TO_MQTT_ACTION')
broker = os.getenv('REACT_TO_MQTT_BROKER')
port = int(os.getenv('REACT_TO_MQTT_PORT'))
topic = os.getenv('REACT_TO_MQTT_TOPIC')
client_prefix = os.getenv('REACT_TO_MQTT_CLIENTPREFIX')
client_id = str(uuid.uuid4())
client_name = f"{client_prefix}-{client_id}"

def connect_mqtt():
    def on_connect_routine(client, userdata, flags, rc):
        if rc == 0:
            print("connected successfully")
        else:
            print("failed to connect!")
    
    client = mqtt.Client(client_name)
    client.on_connect = on_connect_routine
    client.connect(broker, port)
    return client


def on_message_routine(client, userdata, msg):
    os.system(action)

def run():
    subscriber_instance = connect_mqtt()
    subscriber_instance.subscribe(topic)
    subscriber_instance.on_message = on_message_routine
    subscriber_instance.loop_forever()


if __name__ == '__main__':
    run()