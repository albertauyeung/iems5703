import socket
import sys
import logging

# Set default socket timeout
socket.setdefaulttimeout(5)

# Set up logging
logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s] [%(processName)s] [%(threadName)s] : %(message)s',
    level=logging.INFO)

if __name__ == "__main__":
    
    # Read parameters from command line
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    url = sys.argv[3]

    # Create socker and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    logging.info("Connected to server at ({}, {:d})".format(
        server_ip, server_port))

    # Send URL to the server
    data = url + "[END]"
    s.sendall(data.encode("utf-8"))
    logging.info("URL sent to the server")

    # Receive result from server
    data = ""
    while True:
        r = s.recv(2048)
        data += r.decode("utf-8")
        if len(r) == 0:
            break

    # Output server response
    logging.info("Server response: {}".format(data))
