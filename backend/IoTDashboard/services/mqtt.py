import paho.mqtt.client as mqtt
from .logger import logger
from ..settings import MQTT_BROKER_URL,MQTT_USERNAME, MQTT_PASSWORD


class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client(client_id="ma")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.broker_host = MQTT_BROKER_URL


    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected successfully to broker")
        else:
            logger.error("Failed to connect to broker")
    
    def on_message(self, client, userdate, msg):
        #Call celery task to ingest to data
        topic = msg.topic
        decoded = str(msg.payload.decode("utf-8"))
        logger.info(f"{topic} has received: {decoded}")

    def connect(self):
        self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.client.connect(host=self.broker_host, port=5683, keepalive=60)
        self.client.loop_start()

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

    def publish(self, topic="test_topic", payload="test"):
        self.client.publish(topic=topic, payload=payload)
    
    def start_mqtt_listener(self):
        topic = "test_topic"
        self.connect()
        self.client.subscribe(topic)
        self.client.loop_forever()
