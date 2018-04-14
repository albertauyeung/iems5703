import tkinter as tk
from queue import Queue
import threading
import time
import random


def generate_text(queue):
    """
    Generate a random number, convert it to a string,
    and then put it into the queue
    """
    while True:
        i = random.randint(0, 9999)
        queue.put(str(i))
        time.sleep(1)


class Application(tk.Frame):
    """The GUI main application"""

    def __init__(self, master, queue):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.queue = queue

    def create_widgets(self):
        """Create a textarea with a scrollbar"""
        self.textarea = tk.Text(self, height=20, width=100)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.textarea.pack(side="left", fill="both", expand=True)

        # Execute the get update
        self.after(0, self.get_update)

    def get_update(self):
        """
        A function that will keep getting data from the queue
        and then insert it into the text area
        """
        try:
            # Use non-blocking get here to avoid blocking the UI thread
            text = self.queue.get(block=False)
            text = "Received: {}...\n".format(text)
            self.textarea.insert(tk.END, text)
        except:
            # Catch the empty queue exception here
            pass
        # Wait for a while before checking the queue again
        self.after(10, self.get_update)

# Create a queue
q = Queue()

# Create a new thread to generate the random numbers
worker_thread = threading.Thread(target=generate_text, args=(q,), daemon=True)
worker_thread.start()

# Create the main window and start the application
root = tk.Tk()
app = Application(root, q)
app.mainloop()
