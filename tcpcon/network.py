import threading
import sys
from .terminate import TerminateCause

BUFFER_SIZE = 4096


class NetworkReadThread(threading.Thread):
    def __init__(self, terminate_queue, net_socket):
        threading.Thread.__init__(self)
        self.terminate_queue = terminate_queue
        self.net_socket = net_socket

    def run(self):
        while True:
            data = self.net_socket.recv(BUFFER_SIZE)
            if len(data) == 0:  # Connection was closed
                break
            sys.stdout.buffer.write(data)
            sys.stdout.flush()
        self.terminate_queue.put(TerminateCause.Closed)
