from library.brokerservice import BrokerService
import RPi.GPIO as GPIO


# act on switch message
def switch(msg):
    if msg == "on":
        GPIO.output(PIN_MAGNET, True)
    if msg == "off":
        GPIO.output(PIN_MAGNET, False)


try:
    broker = BrokerService('magnet')

    PIN_MAGNET = int(broker.config['gpio']['magnet'])

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_MAGNET, GPIO.OUT)

    # subscribe to the "magnet/switch" topic to forward messages to our callback function
    broker.subscribe('switch', switch)
    broker.loop()
finally:
    GPIO.cleanup()
