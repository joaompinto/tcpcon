import argparse
from .netcat import NetCatClient


class CommandArgs:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Process some integers.")
        parser.add_argument("-v", help="Set verbose mode", action="store_true")
        parser.add_argument("hostname", help="Connect to hostname", metavar="HOSTNAME")
        parser.add_argument("port", help="Using port", metavar="PORT")
        parser.add_argument(
            "-t", help="Max connection timeout (secs)", metavar="TIMEOUT"
        )
        self.parser = parser

    def parse(self):
        self.args = self.parser.parse_args()

    def run(self):
        if self.args.hostname:
            if self.args.v:
                print(f"* Connecting to {self.args.hostname}, port {self.args.port}")
            netcat = NetCatClient(self.args.hostname, self.args.port)
            netcat.connect()
            if self.args.v:
                print("* Connected")
            netcat.interactive_shell()
