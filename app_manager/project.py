import os
from config import config
from utils import execute


class Project(object):
    def __init__(self, name):
        self.name = name

    def setup(self):
        os.chdir(config.get_directory(self.name))
        for command in config.get_setup_commands(self.name):
            execute(command)

    def start(self):
        os.chdir(config.get_directory(self.name))
        execute('screen -dmS {} {}'.format(self.name, config.get_start_command(self.name)))

    def stop(self):
        execute('screen -S {} -X stuff $\'\cc\''.format(self.name))

    def attach(self):
        execute('screen -r {}'.format(self.name))
