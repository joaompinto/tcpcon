import socket
import sys
from queue import Queue
from .network import NetworkReadThread
from .keyboard import KeyboardReadThread
from .terminate import TerminateCause


class TcpClient:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.terminate_queue = Queue()

    def connect(self, timeout=10.0):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((self.hostname, int(self.port)))
        s.settimeout(None)
        self.net_socket = s

    def create_thread(self, thread_class):
        user_thread = thread_class(self.terminate_queue, self.net_socket)
        user_thread.daemon = True
        user_thread.start()

    def send_from_stdin(self):
        while True:
            data = sys.stdin.buffer.read()
            if len(data) == 0:
                break
            self.net_socket.sendall(data)

    def interactive_shell(self):

        # Create network read
        if sys.stdin.isatty():
            self.create_thread(KeyboardReadThread)
        else:
            self.send_from_stdin()

        self.create_thread(NetworkReadThread)

        # Pause the main thread waiting for a network or keyboard terminate reason
        terminate_reason = self.terminate_queue.get()

        if terminate_reason == TerminateCause.User:
            print("\n*** Terminated by CTRL+C ***", file=sys.stderr)
        if terminate_reason == TerminateCause.Closed:
            print("\n* Remote host closed the connection", file=sys.stderr)
