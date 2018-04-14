from redis import StrictRedis

r = StrictRedis(host='localhost', port=6379)

while True:
    item = r.blpop('channel_01')
    print(item)
