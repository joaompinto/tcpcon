import argparse
from .netcat import NetCatClient


class CommandArgs:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Process some integers.")
        parser.add_argument("-v", help="Set verbose mode", action="store_true")
        parser.add_argument("-c", help="Connect to hostname", metavar="HOSTNAME")
        parser.add_argument("-p", help="Using port", metavar="PORT")
        parser.add_argument(
            "-t", help="Max connection timeout (secs)", metavar="TIMEOUT"
        )
        self.parser = parser

    def parse(self):
        self.args = self.parser.parse_args()

    def validate(self):
        if self.args.c and not self.args.p:
            print("When using -c must provide a port with -p")
            exit(2)

    def run(self):
        if self.args.c:
            if self.args.v:
                print(f"* Connecting to {self.args.c}, port {self.args.p}")
            netcat = NetCatClient(self.args.c, self.args.p)
            netcat.connect()
            netcat.wait_for_input()
