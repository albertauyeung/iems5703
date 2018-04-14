import os
import sys
import socket
import urllib.request
import hashlib
import logging
import threading
from queue import Queue
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from keras_squeezenet import SqueezeNet
from keras.applications.imagenet_utils import preprocess_input
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
import tensorflow as tf

# Set up logging
logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s] [%(processName)s] [%(threadName)s] : %(message)s',
    level=logging.DEBUG)


class ClientThread(threading.Thread):

    def __init__(self, graph, model, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.graph = graph
        self.model = model

    def run(self):
        """Get client connection from queue"""
        while True:
            soc, address = self.queue.get()
            self.handle_client(soc, address)

    def handle_client(self, soc, address):
        """Handle one client connection"""
        logging.info("Thread {} starts".format(self.name))

        # Receive the URL from the client
        data = ""
        while True:
            chunk = soc.recv(2048).decode("utf-8")
            data += chunk
            if "[END]" in data:
                break

        url = data.replace("[END]", "")
        logging.info("Client submitted URL: {}".format(url))

        # Download the image
        m = hashlib.md5()
        m.update(url.encode("utf-8"))
        file_name = "images/{}.jpg".format(m.hexdigest())
        urllib.request.urlretrieve(url, file_name)
        logging.info("Image saved to {}".format(file_name))

        # Apply the model and get the result
        result = self.recognize(file_name)
        result = str(result)
        logging.info("SqueezeNet result: %s" % result)

        # Send back the result to the client and close connection
        soc.sendall(result.encode("utf-8"))
        soc.shutdown(socket.SHUT_RDWR)
        soc.close()
        logging.info("Client connection closed")

    def recognize(self, file_name):
        """Apply the SqueezeNet model to the image"""
        with self.graph.as_default():
            img = image.load_img(file_name, target_size=(227, 227))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            preds = self.model.predict(x)
            preds = decode_predictions(preds)
            label = preds[0][0][1]
            proba = preds[0][0][2]
            return (label, proba)


def handle_request(queue):
    """
    A function that will be executed by a child process.
    It will keep on getting client connection from a queue.
    """
    model = SqueezeNet()
    g = tf.get_default_graph()
    thread_queue = Queue()
    for i in range(4):
        t = ClientThread(g, model, thread_queue)
        t.start()

    # Get client from the process queue,
    # and then put it into the thread queue
    while True:
        soc, address = queue.get()
        logging.info("Received {}".format(str(address)))
        thread_queue.put((soc, address))


if __name__ == "__main__":

    # Get arguments from command line
    port = int(sys.argv[1])
    num_proc = int(sys.argv[2])

    # Create server socket for listening
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(10)
    logging.info("Start listening for connections on port {}".format(port))
    queue = mp.Queue()

    # Spawn child processes
    for i in range(num_proc):
        p = mp.Process(target=handle_request, args=(queue, ))
        p.start()
        logging.info("Created process {}".format(p.name))

    # Accept client connections and put them into the queue
    while True:
        client_socket, address = server_socket.accept()
        logging.info("Client {} connected.".format(str(address)))
        queue.put((client_socket, address))
