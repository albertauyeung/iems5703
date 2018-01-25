import time
from threading import Thread

def print_squares(n):
    print(n*n)

start_time = time.time()

threads = []
for i in range(100):
    t = Thread(target=print_squares, args=(i+1,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Using threads:", time.time() - start_time)

start_time = time.time()
for i in range(100):
    print_squares(i+1)

print("Sequential:", time.time() - start_time)