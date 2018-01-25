import threading
from threading import Thread

class Counter:
    def __init__(self):
        self.lock = threading.Lock()
        self.count = 0
    def increment(self):
        with self.lock:
            self.count += 1

def add_two(counter):
    for i in range(2):
        counter.increment()

counter = Counter()
threads = []
for i in range(5):
    t = Thread(target=add_two, args=(counter,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(counter.count)

