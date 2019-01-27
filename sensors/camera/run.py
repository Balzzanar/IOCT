import tempfile
import base64
from picamera import PiCamera
import time
from library.brokerservice import BrokerService

broker = BrokerService('camera')
while 1:
    # try to get a new image from the camera
    camera = PiCamera()
    try:
        file = tempfile.NamedTemporaryFile(suffix='image.jpg')
        camera.capture(file.name)
        content = file.read()
        file.close()
        broker.publish("response", base64.b64encode(content))
        pass
    except Exception as exception:
        print(exception)
    finally:
        camera.close()
    time.sleep(10)
