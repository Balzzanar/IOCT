from library.brokerservice import BrokerService
import RPi.GPIO as GPIO


# act on switch message
def switch(msg):
    if msg == "on":
        # False means "on", strange, but true
        GPIO.output(PIN_LIGHT, False)
    if msg == "off":
        GPIO.output(PIN_LIGHT, True)


try:
    broker = BrokerService('light')

    PIN_LIGHT = int(broker.config['gpio']['light'])

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_LIGHT, GPIO.OUT)

    # subscribe to the "magnet/switch" topic to forward messages to our callback function
    broker.subscribe('light', switch)
    broker.loop()
finally:
    GPIO.cleanup()
