import time
from redis import StrictRedis

queue = StrictRedis(host='localhost', port=6379)
channel = queue.pubsub()

for i in range(100): 
    message = "Hello {:d}".format(i)
    queue.publish("test", message)
    print("Published {}".format(message))
    time.sleep(1.0)
