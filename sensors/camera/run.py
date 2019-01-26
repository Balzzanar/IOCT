import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import configparser


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe(config['mqtt-broker']['topic-prefix'] + "/" + config['device']['name'])
    client.subscribe("iotc/box1")
    print("subscribed to iotc/box1")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


config = configparser.ConfigParser()
config.read('../../config.ini')

client = mqtt.Client(protocol=mqtt.MQTTv31)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set()
client.tls_insecure_set(config['mqtt-broker']['host'])
client.connect(config['mqtt-broker']['host'], int(config['mqtt-broker']['port']), 60)

publish.single("iotc/box1", "Hello World!", hostname=config['mqtt-broker']['host'])

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
