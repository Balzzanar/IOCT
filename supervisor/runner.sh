#!/bin/bash

SCRIPT=$1

cd /home/pi/IOCT
export PYTHONPATH=.
python3 "${SCRIPT}/run.py"
