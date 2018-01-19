# Assignment 1 - Socket Programming

* Full Mark: **100** (**10%** of the course assessment scheme)
* Deadline: 10th February, 2018
* Submission: See instructions below
* NOTE: The assignment must be finished using Python

## Overview

In this assignment, you will practice how to develop a server and a client program that communicate with each other using TCP.

The **server** provides a service that assigns [part-of-speech tags](http://en.wikipedia.org/wiki/Part-of-speech_tagging) to a sentence received from the client, and sends the results back to the client.

The **client** reads a English sentence that is stored in a text file, and then send the sentence to the server. Upon receiving the results, it should print in to the standard output.

## Detailed Descriptions

### Server

In this assignment, you should use Python's `socket` module to implement data communication using TCP.

The server should accept client connections on port `55703`. Once the server has accepted a connection, it should start receiving data from the client. Here, you will have ot make sure that the server has received the full sentence from the client, and that the connection is still alive (such that you can send response back to the client).

In the server, you should assume that the message from the client will end with a special string `[END]`. Also, you server should follow the requirements below:

1. It only needs to handle one client at a time (other clients can be put in the queue).
2. It only needs to use blocking functions.
3. It has to use a buffer size of `2048`, and has to continue to read data from client until `[END]` is received
4. When a client has connected, it should display a message `"Client (<client_address>) connected."`
5. The results should be sent in the form of a [JSON encoded](http://docs.python.org/3/library/json.html) string.
6. No ending special string has to be sent to the client, because the client will know that everything is received when the server disconnects.
7. After sending the result to the client, or in case the connection with the client is broken or lost, it should display a message `"Client disconnected"`, and go on to server the next client.
8. The server's port number should be configurable using an argument when executing the script.
9. The server should print out the sentence submitted by the client in the standard output.

Regarding the service of POS tagging, you should use the functions in the [Natural Language Toolkit (NLTK)](http://www.nltk.org/book/ch05.html) to perform tokenization and POS tagging. Read the documentation for mode details. An example is shown below:

    :::python
    import nltk
    
    # Breaks a sentence into tokens
    tokens = nltk.word_tokenize("I love socket programming in Python!")
    # Now tokens = ['I', 'love', 'socket', 'programming', 'in', 'Python', '!']

    # Predicts the POS tags of each token
    tagged = nltk.pos_tag(tokens)
    # tagged = [
    #   ('I', 'PRP'), ('love', 'VBP'), ('socket', 'NN'),
    #   ('programming', 'NN'), ('in', 'IN'),
    #   ('Python', 'NNP'), ('!', '.')
    # ]

You should encode the result of the `nltk.pos_tag` function call using JSON (hint: check out the `json` module in Python, in particular the `json.dumps()` function).

The server should be executed by providing a port number as follows:

    :::bash
    $ python3 server.py 55703
    Listening for incoming connections on port 55703
    ...

### Client

You probably already know what the client should do given the descriptions of the server above. More specifcally, the client should follow the requirements below:

1. Accepts server address, server port number and the path to a text file as arguments when it is executed
2. It should read the sentence contained in the text file (you can assume that the file is encoded in UTF-8)
3. It should attempt to connect to the server using the specified address and port number. Once connected, it should display a message `"Connected to server."`
4. It should terminate when it cannot connect to the server after printing a message: `"Cannot connect to server at <address>:<port>"`
5. Once connected, it should send the sentence to the server, and append `[END]` at the end to let the server know that no more data will be sent.
6. On receiving the result from the server, it should decode the JSON data into a list in Python
7. It should print out the original sentence in one line, with each token separated by a semicolon.
8. It should then print out the list of POS tags, with each separated by a semicolon.

The client should be executed as follows (assuming that a `server.py` is already executed in the same machine and on port `55703`, and the file containing the sentence is named `sentence.txt` in the same folder as the script):

    :::bash
    $ python3 client.py localhost 55703 sentence.txt

## Example

Below shows an example of running the `server.py` and `client.py` scripts. Your program should follow the format of the output below. Let's assume that the sentence stored in the text file is `"I love socket programming in Python!"`.

Executing `server.py`:

    :::bash
    $ python3 server.py 55703
    Listening for incoming connections on port 55703
    Client 192.168.1.12 connected.
    I love socket programming in Python!
    Client disconnected.

Executing `client.py`:

    :::bash
    $ python3 client.py localhost 55703 sentence.txt
    Connected to server.
    I ; love ; socket ; programming ; in ; Python ; !
    PRP ; VBP ; NN ; NN ; IN ; NNP ; .

## Submission

Prepare the following python scripts:

1. The server script `server.py`
2. The client script `client.py`

Put the two scripts in a folder named using your student ID, and compress the folder using zip, resulting in a compressed file `<student_id>.zip` (e.g. `12345678.zip`). Submit this file to the assignment submission page in Blackboard.
