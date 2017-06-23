import os
import subprocess


def execute(command):
    return subprocess.check_call(command, shell=True)
