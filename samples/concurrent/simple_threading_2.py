from threading import Thread


def print_hello(n):
    """A function that a thread will execute"""
    print("Hello! %d" % n)

# Create 5 threads
threads = []
for i in range(5):
    t = Thread(target=print_hello, args=(i,))
    t.start()
    threads.append(t)

# Wait until all threads are finished
for t in threads:
    t.join()

