#!/bin/bash

SCRIPT=$1

if [ $SCRIPT == "camera" ]; then
	/home/pi/IOCT
	export PYTHONPATH=.
	python3 sensors/camera/run.py
fi

if [ $SCRIPT == "temperature" ]; then
	/home/pi/IOCT
	export PYTHONPATH=.
	python3 sensors/temperature/run.py
fi

if [ $SCRIPT == "magnet" ]; then
	cd /home/pi/IOCT
	export PYTHONPATH=.
	python3 actuators/magnet/run.py
fi

