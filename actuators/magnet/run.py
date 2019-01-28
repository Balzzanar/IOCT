from library.brokerservice import BrokerService
import RPi.GPIO as GPIO

broker = BrokerService('magnet')

PIN_MAGNET = broker.config['gpio']['magnet']
PIN_LIGHT = broker.config['gpio']['light']

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LIGHT, GPIO.OUT)
GPIO.setup(PIN_MAGNET, GPIO.OUT)


# act on switch message
def switch(msg):
    if msg == "on":
        GPIO.output(PIN_MAGNET, True)
        GPIO.output(PIN_LIGHT, False)
    if msg == "off":
        GPIO.output(PIN_MAGNET, False)
        GPIO.output(PIN_LIGHT, True)


# subscribe to the "magnet/switch" topic to forward messages to our callback function
broker.subscribe('switch', switch)
