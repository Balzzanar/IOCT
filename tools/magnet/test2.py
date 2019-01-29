import RPi.GPIO as GPIO
import time

PIN = 6

try:
    print("init")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    print("on")
    GPIO.output(PIN, True)
    time.sleep(1)
    print("off")
    GPIO.output(PIN, False)
    time.sleep(1)
finally:
    GPIO.cleanup()
