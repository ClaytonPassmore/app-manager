import subprocess
from sys import stdout

from colours import ENDC


def execute(command):
    return subprocess.check_call(command, shell=True)


def write(message, colour=''):
    stdout.write(colour + message + ENDC)


def write_line(message, colour=''):
    write(message + '\n', colour)
