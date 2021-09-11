import threading
import sys
from getch import getch

CONTROL_C = b"\x03"


class KeyboardReadThread(threading.Thread):
    def __init__(self, terminate_queue, net_socket):
        threading.Thread.__init__(self)
        self.terminate_queue = terminate_queue
        self.net_socket = net_socket

    def run(self):

        while True:
            read_key = getch()

            if read_key == b"\r":
                read_key = b"\r\n"

            if read_key == CONTROL_C:
                break

            self.sendall(read_key)
        self.terminate_queue.put(None)

    def sendall(self, content):
        sys.stdout.buffer.write(content)
        sys.stdout.flush()
        """ try to send to the remote end """
        try:
            self.net_socket.sendall(content)
        except Exception as ex:
            print(ex, file=sys.stderr)
            self.terminate_queue.put(None)
