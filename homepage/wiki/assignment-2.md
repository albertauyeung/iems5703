# Assignment 2 - A Multi-process TCP Server

* Full Mark: **100** (**10%** of the course assessment scheme)
* Deadline: 3rd March, 2018
* Submission: See instructions below
* NOTE: The assignment must be finished using Python

## Overview

In this assignment, you will implement a TCP server that can handle multiple clients at the same time using the **pre-fork worker model**. The server provides an **object recognition** function, i.e. the client will send an image to the server, and the server will attempt to recognize what is inside the picture and send back the answer to the client.

You will have to implement both the **server** and the **client** in this assignment.

## Detailed Descriptions

### Logging

In this assignment, you should use the `logging` module to display log messages. **NO** `print` statements should be present in your programs. Since we will use multiple processes and multiple threads in this assignment, we will log the following information in each log messages:

1. Time of the log
2. The process that creates that log
3. The thread that creates that log
4. The message of the log

You can use the following formatting string when initializing the logger:

    :::python
    logging.basicConfig(
        format='[%(asctime)s] [%(levelname)s] [%(processName)s] [%(threadName)s] : %(message)s',
        level=logging.INFO)


### Server

You will implement a pre-fork TCP server in this assignment. The diagram below illustrates the server architecture:

<center>
<img src="files/assignment-2.png" width="90%">
</center>

The following steps describe what the server will do:

1. Your server script should accept **two** command line arguments: 1) **port number** on which it listens for incoming connection, 2) **number of processes** to create on start to handle client requests.
2. Create a socket and listen on `("0.0.0.0", port_number)`, where `port_number` is the one provided when executing the script.
3. Create the specific number of **child processes**. They will wait for the main process to pass client sockets and client addresses to them when new clients are connected. (Hint: use the `multiprocessing.Queue` class)
4. Each child process should create a **thread pool** with a maximum of **4 workers**.
5. When a new client connects to the server, the client socket and client address will be passed to one of the child processes, and the child process will create a **new thread** for handling the client request by submitting it to the thread pool.
6. The client will send a URL of an image to the server (see client description below). It will use `[END]` to idnciate the end of the image.
7. The thread receiving the URL will perform the following:
    - **Download** the image from the URL and save it to a local file in a folder named `images` (you should generate a unique file name because two or more files may be downloaded at the same time)
    - **Process** the image using `SqueezeNet` to recognize the object inside the image
    - **Return** the most probable result to the client. The message should be a string in the form of `("object", probability)`. E.g. `("airliner", 0.995)`.
    - **Close** the client connection. **NOTE**: you should call `socket.shutdown()` before `socket.close()` in the thread, otherwise the connection may not disconnect immediately.

Below is an example run of the server:

    :::bash
    $ python3 server.py 50001 4
    [2018-02-11 08:45:22,509] [INFO] [MainProcess] [MainThread] : Start listening for connections on port 50001
    [2018-02-11 08:45:22,523] [INFO] [MainProcess] [MainThread] : Created process Process-1
    [2018-02-11 08:45:22,531] [INFO] [MainProcess] [MainThread] : Created process Process-2
    [2018-02-11 08:45:22,539] [INFO] [MainProcess] [MainThread] : Created process Process-3
    [2018-02-11 08:45:22,544] [INFO] [MainProcess] [MainThread] : Created process Process-4
    [2018-02-11 08:23:38,637] [INFO] [MainProcess] [MainThread] : Client ('127.0.0.1', 49264) connected.
    [2018-02-11 08:23:38,641] [INFO] [Process-3] [Thread-4] : Received Client ('127.0.0.1', 49264).
    [2018-02-11 08:23:38,645] [INFO] [Process-3] [Thread-4] : Client submitted URL http://....
    [2018-02-11 08:23:38,705] [INFO] [Process-3] [Thread-4] : Image saved to images/images0001.jpg
    [2018-02-11 08:23:39,689] [INFO] [Process-3] [Thread-4] : SqueezeNet result: ("airliner", 0.995)
    [2018-02-11 08:23:39,983] [INFO] [Process-3] [Thread-4] : Client connection closed

As you can see in the example above, the server should create log messages for:

1. When it starts listening for connections
2. When a new process has been created
3. When a new client has connected to the main process
4. When a new thread in a child process has received a new client from the main process
5. When the thread has received the URL from the client
6. When the thread has downloaded the image successfully
7. When the thread has got a result from SqueezeNet
8. When the client connection is closed

Make sure that you test your server by issuing multiple requests to it and see if the processes take turn to process client requests, and also that new threads are created when a new client connects.

### Client

The client is a simple script that sends a URL of an image to the server, receives the result and display the result to the user. The requirements of the client are listed below:

1. The client script should accepts **3** arguments: 1) the IP address or host name of the server, 2) the port number on which the server listens for connections, and 3) the URL of the image for processing
2. Once connected to the server, it should send the URL to the server, append the `[END]` string to the URL such that the server knows when to stop receiving data from the client
3. Wait for the server to send back the result, and display the result on the screen

In the client script, you also need to use the `logging` module to create log messages. Use the same log format as in the sever. Below is an example run of the client script.

    :::bash
    $ python3 client.py localhost 50001 https://media1.britannica.com/eb-media/57/93557-004-13E80176.jpg
    [2018-02-11 09:22:53,512] [INFO] [MainProcess] [MainThread] : Connected to server at (localhost, 50000)
    [2018-02-11 09:22:53,512] [INFO] [MainProcess] [MainThread] : URL sent to the server
    [2018-02-11 09:22:54,235] [INFO] [MainProcess] [MainThread] : Server response: ('airliner', 0.99504316)

### Using SqueezeNet

In order to use [SqueezeNet](https://github.com/rcmalli/keras-squeezenet), you need to first install `tensorflow` and `keras`. Normally, the following commands will install everything required. If not successful, consult the documentations of these libraries and check if specific steps are required for your platform.

    :::bash
    $ pip3 install tensorflow
    $ pip3 install keras
    $ pip3 install keras_squeezenet

In Tensorflow, computation happends in a **graph**. When using multi-threading with Tensorflow, there might be problems when different threads attempt to perform computation on the same graph. Therefore, you should take the following steps to ensure that every time the same graph is used to process the image submitted.

Firstly, in each child process, create a variable that wholes the default graph in tensorflow:

    :::python
    import tensorflow as tf
    ...
    graph = tf.get_default_graph()

Then, when creating a new thread, pass the graph into the thread. You may also create an instance of the SqueezeNet model in the child process and pass it into the thread too.

When you want to generate a prediction using the SqueezeNet model, use the `with` statement with the graph:

    :::python
    with graph.as_default():
        ...
        predictions = model.predict(...)

## Submission

Prepare the following python scripts:

1. The server script `server.py`
2. The client script `client.py`

Put the two scripts in a folder named using your student ID, and compress the folder using zip, resulting in a compressed file `<student_id>.zip` (e.g. `12345678.zip`). Submit this file to the assignment submission page in Blackboard.
