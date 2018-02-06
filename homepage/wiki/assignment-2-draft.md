# Assignment 2 - A Multi-process TCP Server

* Full Mark: **100** (**10%** of the course assessment scheme)
* Deadline:
* Submission:

## Overview

In this assignment, you will implement a TCP server that can handle multiple clients at the same time using the **pre-fork worker model**. The server provides an **object recognition** function, i.e. the client will send an image to the server, and the server will attempt to recognize what is inside the picture and send back the answer to the client.

You will have to implement both the **server** and the **client** in this assignment.

## Detailed Descriptions

### Client


An image should be first converted into bytes before sending.

Firstly, convert the image into base64 encoding, which is a string representation of the image. Add the `[END]` string to the end of the base64 string, and then send the whole string to the server.


### Server

Create 4 processes to handle client requests. Your main process (the main program) will be responsible for accepting connections from clients, and then pass the client sockets and client addresses to the 4 workers. Therefore, once you server is executed, it always has **5** processes running.

Use the `ThreadPoolExecutor` class to limit the maximum number of worker to **3**.

### Installing Tensorflow and Keras


### Installing SqueezeNet

pip install keras_squeezenet
https://github.com/rcmalli/keras-squeezenet

### Notes

Concurrent use of tensorflow/keras models
create a global variable graph, and use a lock such that it can only be accessed by a single thread at a time


## Submission

Prepare the following python scripts:

1. The server script `server.py`
2. The client script `client.py`

Put the two scripts in a folder named using your student ID, and compress the folder using zip, resulting in a compressed file `<student_id>.zip` (e.g. `12345678.zip`). Submit this file to the assignment submission page in Blackboard.
