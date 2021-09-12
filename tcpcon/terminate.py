from enum import Enum, auto


class TerminateCause(Enum):
    User = auto()  # User interrupted the the session
    Closed = auto()  # Connection was closed from the remote host
    Broken = auto()  # Connection interrupted while attempting to write
