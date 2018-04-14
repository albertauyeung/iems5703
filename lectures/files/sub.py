from redis import StrictRedis

queue = StrictRedis(host='localhost', port=6379)
p = queue.pubsub()
p.subscribe('test')
p.get_message()

while True:
    message = p.get_message()
    if message:
        print("Subscriber: {}".format(message['data'].decode("utf-8")))
