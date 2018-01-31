from threading import Thread
from time import sleep

def print_hello():
    sleep(0.2)
    print("Hello!")

threads = []
for i in range(5):
    t = Thread(target=print_hello, daemon=True)
    t.start()

