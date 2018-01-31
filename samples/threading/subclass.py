from threading import Thread

class SquareThread(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        print(self.n * self.n)

for i in range(5):
    t = SquareThread(i)
    t.start()

