from .celery import celery_app, ingest_temperature_data_task, publish_temperature_data_task
from .services.mqtt import MQTTClient


@celery_app.task(name="test_task")
def test_task() -> None:
    print("This is an async test task..")


@celery_app.task(name=publish_temperature_data_task)
def publish_temperature_data():
    # For each device: Generate random temperate data between 20 - 30 C
    mqtt_client = MQTTClient()
    mqtt_client.connect()
    try:
        topic = "your_topic"
        message = "your_message"
        mqtt_client.publish()
        print(f"Published to topic")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        mqtt_client.disconnect()


@celery_app.task(name=ingest_temperature_data_task)
def ingest_temperate_data():
    # MQTT subscriber on message received calls this task passing t he temperature data to be ingested in db.
    pass
