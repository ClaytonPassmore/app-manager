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

    def start(self, start_attached=False):
        os.chdir(config.get_directory(self.name))

        opts = '-dmS'
        if start_attached:
            opts = '-S'

        execute('screen {} {} {}'.format(opts, self.name, config.get_start_command(self.name)))

    def stop(self):
        execute('screen -S {} -p 0 -X stuff $\'\cc\''.format(self.name))

    def attach(self):
        execute('screen -r {}'.format(self.name))
