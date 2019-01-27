#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

print GPIO.RPI_INFO
print GPIO.VERSION

# physical pins on GPIO board:
TemprPin = 36
ObstaclePin = 37

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(TemprPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if (0 == GPIO.input(ObstaclePin)):
            print "Barrier is detected!"
        tempr = GPIO.input(TemprPin)
        print "Temperature is: ", tempr
        time.sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

