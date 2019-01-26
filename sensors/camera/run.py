import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import configparser
import tempfile
import os
import base64
from picamera import PiCamera


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(config['mqtt-broker']['topic-prefix'] + "/" + config['device']['name'] + "/camera/capture")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # try to get a new image from the camera
    camera = PiCamera()
    try:
        file = tempfile.NamedTemporaryFile(suffix='image.jpg')
        camera.capture(file.name)
        content = file.read()
        file.close()
        os.unlink(file.name)
        publish.single(config['mqtt-broker']['topic-prefix'] + "/" + config['device']['name'] + "/camera/response",
                       base64.b64encode(content), hostname=config['mqtt-broker']['host'])
        pass
    finally:
        camera.close()


config = configparser.ConfigParser()
config.read('../../config.ini')

client = mqtt.Client(protocol=mqtt.MQTTv31)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.tls_set(config['mqtt-broker']['certificate'])
    client.tls_insecure_set(config['mqtt-broker']['host'])
    port = int(config['mqtt-broker']['tls-port'])
    pass
except(e):
    port = int(config['mqtt-broker']['port'])

client.connect(config['mqtt-broker']['host'], port, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
