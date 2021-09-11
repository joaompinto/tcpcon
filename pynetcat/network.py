import threading
import sys
import socket

BUFFER_SIZE = 4096


class NetworkReadThread(threading.Thread):
    def __init__(self, terminate_queue, net_socket):
        threading.Thread.__init__(self)
        self.terminate_queue = terminate_queue
        self.net_socket = net_socket

    def run(self):
        while True:
            try:
                data = self.net_socket.recv(BUFFER_SIZE)
            except socket.timeout:
                data = ""
            if len(data) == 0:  # Connection was closed
                break
            sys.stdout.buffer.write(data)
            sys.stdout.flush()
        self.terminate_queue.put(None)
