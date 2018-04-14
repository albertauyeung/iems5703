import time
import curses
import threading
from threading import Lock
from queue import Queue


def listen_from_network(queue):
    i = 0
    while True:
        queue.put((0, 0, str(i)))
        time.sleep(0.5)
        i += 1


def ui(stdscr, queue):
    while True:
        # See if we have something in the queue for display
        try:
            y, x, text = queue.get(block=False)
            stdscr.addstr(y, x, " " * 80)
            stdscr.addstr(y, x, text)
        except:
            pass

        # See if we have any user input 
        try:
            stdscr.nodelay(1)
            key = stdscr.getkey()
            queue.put((1, 0, "User pressed: {}".format(key)))
        except:
            pass
        
        time.sleep(0.01)


def main(stdscr):
    queue = Queue()
    listen_thread = threading.Thread(
        target=listen_from_network, args=(queue,))
    ui_thread = threading.Thread(
        target=ui, args=(stdscr, queue))

    listen_thread.start()
    ui_thread.start()
    
    listen_thread.join()
    ui_thread.join()

curses.wrapper(main)
