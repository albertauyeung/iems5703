from threading import Thread


def print_hello():
    """A function that a thread will execute"""
    print("Hello!")

# Create 5 threads
threads = []
for i in range(5):
    t = Thread(target=print_hello)
    t.start()
    threads.append(t)

# Wait until all threads are finished
for t in threads:
    t.join()

