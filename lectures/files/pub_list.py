import time
from redis import StrictRedis

r = StrictRedis(host='localhost', port=6379)

for i in range(100):
    message = 'Message {:d}'.format(i)
    r.rpush('channel_01', message.encode("utf-8"))
    print('Pushed: {}'.format(message))
    time.sleep(1.0)
