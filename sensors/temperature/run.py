import time
from library.brokerservice import BrokerService

broker = BrokerService('temperature')
while 1:
    # TODO read temperature
    broker.publish('current', '100')
    time.sleep(10)
