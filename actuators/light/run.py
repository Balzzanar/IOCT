from library.brokerservice import BrokerService
import RPi.GPIO as GPIO


# act on switch message
def switch(msg):
    print(msg)
    print(str(msg))
    if (msg == "on") or (str(msg) == "b'on'"):
        # False means "on", strange, but true
        GPIO.output(PIN_LIGHT, False)
        print("on")
        print(PIN_LIGHT)
    if (msg == "off") or (str(msg) == "b'off'"):
        GPIO.output(PIN_LIGHT, True)
        print("off")
        print(PIN_LIGHT)


try:
    broker = BrokerService('light')

    PIN_LIGHT = int(broker.config['gpio']['light'])

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_LIGHT, GPIO.OUT)

    # subscribe to the "light/switch" topic to forward messages to our callback function
    broker.subscribe('switch', switch)
    broker.loop()
finally:
    GPIO.cleanup()
