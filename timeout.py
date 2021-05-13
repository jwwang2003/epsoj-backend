# Elgin Park Secondary Online Judge (EPSOJ) - Backend
# timeout.py
# May 13, 2021

"""
Simple timeout function that would limit CPU time of
the compilation and grading process
"""

from contextlib import contextmanager
import signal

class TimeoutException(Exception): pass

@contextmanager
def tlim(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)