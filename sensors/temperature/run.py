import time
from library.brokerservice import BrokerService
from w1thermsensor import W1ThermSensor

broker = BrokerService('temperature')
sensor = W1ThermSensor()

while 1:
    # read the temperature
    temperature = sensor.get_temperature()
    broker.publish('current', temperature)
    time.sleep(10)
