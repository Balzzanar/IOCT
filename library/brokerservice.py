import paho.mqtt.client as mqtt
import configparser
import os


class BrokerService:
    config = None
    client = None
    topics = {}
    topicPrefix = ''

    def __init__(self, topic_name):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), '../config.ini'))

        self.client = mqtt.Client(protocol=mqtt.MQTTv31)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.topicPrefix = self.config['mqtt-broker']['topic-prefix'] + "/" + self.config['device']['name'] + "/"
        if topic_name:
            self.topicPrefix += topic_name + "/"

        try:
            self.client.tls_set(self.config['mqtt-broker']['certificate'])
            self.client.tls_insecure_set(self.config['mqtt-broker']['host'])
            port = int(self.config['mqtt-broker']['tls-port'])
            pass
        except Exception as exception:
            port = int(self.config['mqtt-broker']['port'])

        self.client.username_pw_set(self.config['mqtt-broker']['username'], self.config['mqtt-broker']['password']);
        self.client.connect(self.config['mqtt-broker']['host'], port, 60)

    # subscribe to a topic
    def subscribe(self, topic, callback):
        self.topics[self.topicPrefix + topic] = callback
        self.client.subscribe(topic)

    # publish a message to a topic
    def publish(self, topic, message):
        self.client.publish(self.topicPrefix + topic, message)

    # publish a message to a topic
    def loop(self):
        self.client.loop_forever()

    # The callback for when the client receives a CONNACK response from the server.
    def _on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        for topic, callback in self.topics.items():
            client.subscribe(topic)

    # The callback for when a PUBLISH message is received from the server.
    def _on_message(self, client, userdata, msg):
        for topic, callback in self.topics.items():
            if msg.topic == topic:
                callback(msg.payload)
