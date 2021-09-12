import socket
from queue import Queue
from .network import NetworkReadThread
from .keyboard import KeyboardReadThread


class NetCatClient:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def connect(self, timeout=10.0):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((self.hostname, int(self.port)))
        s.settimeout(None)
        self.net_socket = s

    def interactive_shell(self):
        terminate_queue = Queue()

        net_thread = NetworkReadThread(terminate_queue, self.net_socket)
        net_thread.setDaemon(True)
        net_thread.start()

        kbd_thread = KeyboardReadThread(terminate_queue, self.net_socket)
        kbd_thread.setDaemon(True)
        kbd_thread.start()

        _ = terminate_queue.get()
